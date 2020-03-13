
const grain = {
  state: {
    grain_type: {}
  },
  mutations: {
    SET_GRAIN: (state, grain_type) => {
      state.grain_type = grain_type
    }
  },
  actions: {
    set_grain({ commit }, grain_type) {
      // console.log(grain_type.grain, grain_type.sub_warehous)
      commit('SET_GRAIN', grain_type)
    }
  }
}

export default grain
