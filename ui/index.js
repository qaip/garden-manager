const endpoints = {
  create: (garden) => `create/${garden}`,
  createActivate: (garden) => `create/${garden}/--use`,
  delete: (garden) => `delete/${garden}`,
  deleteForced: (garden) => `delete/${garden}/--force`,

  activate: (garden) => `use/${garden}`,
  newBed: (size) => `new/bed/--size/${size}`,

  seed: (bed, name, count) => `seed/--bed/${bed}/--name/${name}/--count/${count}`,
  listGardens: () => `list`,
  listBeds: () => `list/bed`,
  water: (bed) => `water/--bed/${bed}`,
  waterIntensively: (bed) => `water/--bed/${bed}/--intensive`,

  harvest: (bed) => `harvest/--bed/${bed}`,
  harvestForsed: (bed) => `harvest/--bed/${bed}/--force`,
  harvestAll: () => `harvest/--all`,
  harvestAllForced: () => `harvest/--all/--force`,
};

const transformer = {
  create: ([o]) => o,
  createActivate: ([o]) => o,
  delete: ([o]) => o,
  deleteForced: ([o]) => o,

  activate: ([o]) => o,
  newBed: ([o]) => o,

  seed: ([o]) => o,
  
  /** @type {<T>(o: T[]) => { active: boolean, name: string }[]} */
  listGardens: (o) => o.map(([active, name]) => ({ active: active === '*', name })),
  /** @type {<T>(o: T[]) => { AdultPlants: string, Id: string, LifeFactor: string, Seeds: string, Size: string, SmallPlants: string, Spouts: string }[]} */
  listBeds: ([[o]]) => {
    const [headers, _hr, ...rows] = o.split('\n').map((v) => v.split('  ').filter(Boolean));
    return rows.map((row) => Object.fromEntries(headers.map((header, index) => [header.replaceAll(' ', ''), row[index]])));
  },
  water: ([o]) => o,
  waterIntensively: ([o]) => o,

  harvest: ([o]) => o,
  harvestForsed: ([o]) => o,
  harvestAll: ([o]) => o,
  harvestAllForced: ([o]) => o,
};

/**
 * @type {{[K in keyof endpoints]: (...a: Parameters<endpoints[K]>) => Promise<ReturnType<transformer[K]>> }}
 */
const rest = Object.fromEntries(
  Object.entries(endpoints).map(([action, endpoint]) => [
    action,
    async (...args) =>
      transformer[action](await (await fetch(`http://localhost:8000/api/${endpoint(...args)}/`)).json()),
  ])
);

self.rest = rest;












const val = selector => document.getElementById(selector).value

const create = (classname, text) => {
  const element = document.createElement('div')
  element.classList.add(classname)
  element.innerText = text
  return element
}

const updateBeds = async () => {
  const beds = await rest.listBeds()
  const bedElements = beds.map(bed => {
    const element = document.createElement('bed')
    if (bed.active) element.classList.add('active')
    element.classList.add(`bedid-${bed.Id.trim()}`)
    const id = create('id', bed.Id)
    const seeds = create('seeds', bed.Seeds)
    const spouts = create('spouts', bed.Spouts)
    const small = create('small', bed.SmallPlants)
    const adults = create('adults', bed.AdultPlants)
    const size = create('size', bed.Size)
    element.append(id, seeds, spouts, small, adults, size)
    return element
  })
  const bedBlock = document.querySelector('.beds')
  Array.from(bedBlock.children).forEach(el => el.remove())
  bedBlock.append(...bedElements)
}

const updateGardens = async () => {
  const gardens = await rest.listGardens()
  const gardenElements = gardens.map(garden => {
    const element = document.createElement('garden')
    element.onclick = async () => {
      await rest.activate(garden.name)
      await updateGardens()
      await updateBeds()
    }
    if (garden.active) element.classList.add('active')
    element.innerText = garden.name
    return element
  })
  const gardensBlock = document.querySelector('.gardens')
  Array.from(gardensBlock.children).forEach(el => el.remove())
  gardensBlock.append(...gardenElements)
}

window.onload = async () => {
  await updateGardens()
  await updateBeds()
}


const harvest = bedId => {
  document.querySelector(`bed.bedid-${bedId} .adults`).innerText = '0'
}
const harvestForsed = bedId => {
  Array.from(document.querySelectorAll(`bed.bedid-${bedId} :is(.adults, .small, .spouts, .seeds)`)).forEach(el => el.innerText = '0')
}
const harvestAll = bedId => {
  Array.from(document.querySelectorAll(`bed .adults`)).forEach(el => el.innerText = '0')
}
const harvestAllForced = bedId => {
  Array.from(document.querySelectorAll(`bed :is(.adults, .small, .spouts, .seeds)`)).forEach(el => el.innerText = '0')
}
const update = async () => {
  await updateGardens()
  await updateBeds()
}
