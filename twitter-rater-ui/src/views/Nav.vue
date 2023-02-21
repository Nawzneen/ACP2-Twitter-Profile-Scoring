<template>
  <div class="nav-barr">
    <v-container>
      <v-row class="d-flex justify-center align-center">
        <v-col md="6" align="left">
          <p class="nav_title text-md-h4 text-h6 font-weight-bold">
            Tweetical
          </p></v-col
        >
        <v-col md="6" align="right" class="nav_logo-container">
          <div class="nav_logo">
            <v-img
              src="../assets/thumbnail_CR-Logo.png"
              :width="windowWidth / 27"
              min-width="3rem"
            >
            </v-img>
          </div>
          <div class="nav_logo">
            <v-img
              src="../assets/Ubicomp-Logo.png"
              :width="windowWidth / 27"
              min-width="3rem"
            >
            </v-img>
          </div>
          <div class="nav_logo">
            <v-img
              src="../assets/M3s-logo.png"
              :width="windowWidth / 27"
              min-width="3rem"
            >
            </v-img>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
export default {
  name: "Nav",

  data() {
    return {
      windowWidth: window.innerWidth,
    };
  },

  mounted() {
    this.$nextTick(() => {
      window.addEventListener("resize", this.onResize);
    });
  },

  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },

  methods: {
    onResize() {
      this.windowWidth = window.innerWidth;
    },
  },
};
// export default {
//   name: "Nav",
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Kanit&family=Orbitron:wght@600&family=Unbounded&display=swap");
.nav-barr {
  background-image: linear-gradient(60deg, #23408f, #77aade);
  box-shadow: rgba(0, 0, 0, 0.35) 0px -50px 36px -28px inset;
  color: white !important;
  font-weight: bolder;
  display: flex;
  align-items: center;
  justify-content: center;
}
.logo-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-right: 4rem;
  flex-direction: row;
}
.nav_title {
  font-size: 1.5rem;
  margin: 0 !important;
  font-family: "Kanit", sans-serif;
  font-family: "Orbitron", sans-serif;
  font-family: "Unbounded", cursive;
  text-transform: uppercase;
  letter-spacing: 1px !important;
}

.navigationn {
  justify-content: center;
  display: flex;
  flex-direction: column;
  /* position: relative; */
}
.element {
  position: absolute;
  top: 15%;
  left: 0;
  padding-left: 4rem;
}
.nav_logo {
  padding-right: 1rem;
}
.nav_logo-container {
  display: flex;
  justify-content: right;
  align-items: center;
}
</style>
