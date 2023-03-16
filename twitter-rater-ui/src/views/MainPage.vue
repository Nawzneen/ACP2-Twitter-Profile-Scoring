<template>
  <div>
    <Nav></Nav>
    <v-container>
      <v-container fluid class="main">
        <!-- this row has been moved to this container -->
        <div>
          <!-- <v-row justify="center" align="center" class="my-9">
            <h2 class="text-h6 text-md-h4 mainPage__head">
              Evaluate Your Twitter Profile Credibility!
            </h2>
          </v-row> -->

          <v-row justify="center" align="center">
            <v-col md="8" class="customColumn">
              <h2 class="text-center">
                Evaluate Your Twitter Profile Credibility!
              </h2>

              <!-- <p class="px-4 text-md-body-1 text-body-2"> -->

              <!-- <i
                  >Li J, Paananen V, Suryanarayana SA, Huusko E, Kuutila M,
                  Mäntylä M and Hosio S (2023) <br /><b
                    >It’s Not the Real World, I Don’t Care Much: Investigating
                    Twitter Profile Credibility Using an Online Tool</b
                  >
                  In Proceedings of the ACM Conference on Human Information
                  Interaction and Retrieval (CHIIR ’23)</i
                > -->
              <!--  <br />
                By filling in a short questionnaire study after observing the
                score and the properties that affect it, you will help
                researchers build better tools for understanding online social
                media and critical reading.<br /> -->
              <!-- </p> -->
              <p class="pt-4 px-4 text-md-body-1 text-body-2">
                Analyse your Twitter profile’s credibility using this tool
                created by researchers at the University of Oulu, Finland.
              </p>
              <v-divider class="mb-3 mt-3"></v-divider>

              <p class="pt-4 px-4 text-md-body-1 text-body-2">
                <strong
                  >Type your Twitter username
                  <a
                    style="
                      text-decoration: underline;
                      cursor: default;
                      color: black;
                    "
                  >
                    without</a
                  >
                  the @-mark in the textbox below and click the button to let us
                  compute your credibility score.</strong
                >
              </p>
              <v-container class="textboxContainer">
                <b-icon-at class="iconContainer"></b-icon-at>
                <v-text-field
                  v-model="searchTerm"
                  label="Twitter Username"
                  outlined
                  prevent="getProfile"
                  class="textContainer"
                >
                </v-text-field>
              </v-container>
              <v-expand-transition>
                <v-alert
                  color="red"
                  dark
                  class="errorBox text-md-body-1 text-body-2"
                  v-if="error"
                >
                  User profile was not found or it was unsuitable for
                  evaluation. Check your spelling or try another account!
                </v-alert>
                <v-alert
                  color="red"
                  dark
                  v-else-if="protectedError"
                  class="text-md-body-1 text-body-2"
                >
                  User profile is protected. No tweets can be read and profile
                  cannot be evaluated!
                </v-alert>
                <v-alert
                  color="red"
                  dark
                  v-else-if="tweetError"
                  class="text-md-body-1 text-body-2"
                >
                  User profile has no tweets. Evaluation cannot be done!
                </v-alert>
              </v-expand-transition>
              <v-row justify="center">
                <v-btn
                  color="primary"
                  @click="getProfile"
                  class="mb-3"
                  style="width: 185px"
                  :disabled="loading"
                >
                  <div v-if="!loading" class="text-md-body-1 text-body-2">
                    Evaluate profile
                  </div>
                  <v-progress-circular
                    v-else
                    indeterminate
                    color="green"
                  ></v-progress-circular>
                </v-btn>
              </v-row>
            </v-col>
          </v-row>
          <v-row class="refrence">
            <div>
              <span>More information about the tool:&nbsp;</span>
              <i>
                Li J, Paananen V, Suryanarayana SA, Huusko E, Kuutila M, Mäntylä
                M and Hosio S (2023) <br /><b
                  >It’s Not the Real World, I Don’t Care Much: Investigating
                  Twitter Profile Credibility Using an Online Tool</b
                >
                In Proceedings of the ACM Conference on Human Information
                Interaction and Retrieval (CHIIR ’23)</i
              >
            </div>
          </v-row>
        </div>
      </v-container>

      <Modal v-show="isModalVisible" @close="closeModal" />
    </v-container>
    <!-- Footer -->
    <!-- <v-row>
      <div align="left" class="citation">
        Li J, Paananen V, Suryanarayana SA, Huusko E, Kuutila M, Mäntylä M and
        Hosio S (2023) <br /><b
          >It’s Not the Real World, I Don’t Care Much: Investigating Twitter
          Profile Credibility Using an Online Tool</b
        >
        In Proceedings of the ACM Conference on Human Information Interaction
        and Retrieval (CHIIR ’23)
      </div>
    </v-row> -->
    <!-- To fix the overlapping problem, a second hidden footer with the same properties has been added -->
    <v-footer app bottom padless class="d-none">
      By proceeding to use this application, you consent to being a subject in a
      study by team of researchers from University of Oulu. Your Twitter
      information (only public accounts), results, and feedback will be stored.
      The collected Twitter information is limited to public data available via
      Twitter API. The stored data will be deleted after the study. By
      proceeding to use this application, you consent to being a subject in a
      study by team of researchers from University of Oulu. Your Twitter
      information (only public accounts), results, and feedback will be stored.
      The collected Twitter information is limited to public data available via
      Twitter API. The stored data will be deleted after the study.
    </v-footer>

    <v-footer
      app
      bottom
      v-show="!isModalVisible && !isFooterHidden"
      padless
      class="ftr"
    >
      By proceeding to use this application, you consent to being a subject in a
      study by team of researchers from University of Oulu. Your Twitter
      information (only public accounts), results, and feedback will be stored.
      The collected Twitter information is limited to public data available via
      Twitter API. The stored data will be deleted after the study.
      <v-btn icon dark @click="closeFooter" class="closeFooter-btn">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-footer>
  </div>
</template>

<script>
import Modal from "./Modal.vue";
import Nav from "./Nav.vue";

export default {
  mounted() {
    this.showModal();
  },
  components: {
    Modal,
    Nav,
  },
  name: "MainPage",
  data() {
    return {
      searchTerm: "",
      apiUrl: process.env.VUE_APP_API_URL,
      error: false,
      protectedError: false,
      tweetError: false,
      loading: false,
      isModalVisible: false,
      isFooterHidden: false,
    };
  },
  methods: {
    showModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
    closeFooter() {
      this.isFooterHidden = true;
    },
    getProfile() {
      console.log("Profile search " + this.searchTerm + " " + this.apiUrl);
      if (this.searchTerm) {
        this.loading = true;
        this.error = false;
        this.protectedError = false;
        this.tweetError = false;
        fetch(this.apiUrl + "GetProfile?username=" + this.searchTerm)
          .then((response) => {
            this.loading = false;
            console.log("response", response);
            return response.json();
          })
          .then((data) => {
            console.log(data);
            if (data && !data.protected && data?.tweets?.length > 0) {
              this.$store.commit("setProfile", data);
              this.$router.push("Profile");
            } else if (data?.protected) {
              this.protectedError = true;
            } else if (!data?.tweets || data?.tweets.length == 0) {
              this.tweetError = true;
            } else this.error = true;
          })
          .catch((e) => {
            this.loading = false;
            this.error = true;
            console.log("Error", e);
          });
      } else this.error = true;
    },
    verifyData(profile) {
      return !!profile && !!profile.ml_output;
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Kanit&family=Orbitron:wght@600&family=Unbounded&display=swap");

.main {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: 70vh;
}
.mainPage__head {
  font-family: "Kanit", sans-serif;
  font-family: "Orbitron", sans-serif;
  font-family: "Unbounded", cursive;
}
.textboxContainer {
  position: relative;
}
.textContainer {
  display: block;
}
.iconContainer {
  position: absolute;
  top: 0;
  left: 0;
  display: none;
}
.customColumn {
  border-radius: 10px;
  box-shadow: 0px 5px 5px 5px #888888;
  padding: 20px;
  text-align: justify;
}
.customColumn__header {
  color: #1c326e;
}
.errorBox {
  margin-bottom: 30px;
}
.refrence {
  margin-top: 6vh;
  text-align: left;
}
.refrence span {
  color: #1c326e;
  font-size: 1.1em;
  font-weight: bold;
}
h2 {
  background-image: linear-gradient(60deg, #23408f, #77aade);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.ftr {
  // position: relative;
  font-size: 0.8rem;
  width: 100%;
  padding: 10px 20px;
  background-color: black !important;
  color: white !important;
}
.citation {
  margin-top: 2rem;
  margin-left: 2rem;
  font: 1rem;
}
.closeFooter-btn {
  position: absolute;
  top: 0;
  right: 0;
}
</style>
