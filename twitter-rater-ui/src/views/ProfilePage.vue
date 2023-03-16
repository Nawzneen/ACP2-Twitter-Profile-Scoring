<template>
  <div>
    <Nav></Nav>
    <v-container class="px-3">
      <!-- <v-row justify="center" class="mt-16"> </v-row>
        <v-row justify="center"> </v-row> -->
      <!-- <v-row
        class="d-flex justify-center align-center text-sm-body-2 text-md-body-1"
      >
        <div class="btn-back px-3 py-3">Evaluate another account</div>
      </v-row> -->
      <v-row justify="center" class="mt-md-8" fill-height>
        <!-- This Col is for the left container which includes the Cards  -->
        <v-col class="mt-6 col-md-7 col-12">
          <v-card elevation="2" class="card px-4 py-4">
            <v-row class="card__header mb-2 px-4">
              <v-col class="d-flex justify-start align-center">
                <h3>{{ username }}</h3>
              </v-col>
              <v-col class="card__score-col d-flex justify-end align-center">
                <div align="center " class="card__score-col-container">
                  <div class="d-flex justify-center align-center" v-if="scores">
                    <p class="hidden-sm-and-down">Total Score</p>
                    <div class="card__score-col-circle">
                      {{ scores.score }}/10
                    </div>
                  </div>
                  <div
                    class="d-flex justify-center align-center"
                    v-if="!scores"
                  >
                    No score to show!
                  </div>
                </div>
              </v-col>
            </v-row>
            <v-row>
              <v-col class="col-md-4 col-sm-6 col-12 card-pic_username">
                <v-img
                  class="profile-pic mb-2"
                  height="75"
                  width="75"
                  :src="profile_pic"
                ></v-img>
                <div class="align-left">
                  <div>
                    <!-- <span> <BIconAt color="#264391"></BIconAt> </span
                    > -->
                    <span class="font-weight-bold font-costum">
                      {{ username }}</span
                    >
                  </div>
                  <div v-if="location">
                    <span>
                      <BIconGeoAlt color="#264391"></BIconGeoAlt>
                      <span class="font-weight-bold">{{ location }}</span>
                    </span>
                  </div>
                  <div class="d-flex justify-content align-center flex-column">
                    <div>
                      <span>
                        <BIconCalendar3 color="#264391"></BIconCalendar3>
                      </span>
                      <span class="pl-1 font-weight-bold">{{
                        created_at
                      }}</span>
                    </div>
                    <!-- <span class="pl-1 font-weight-bold">{{created_at}}</span> -->
                  </div>
                </div>
              </v-col>
              <v-col
                class="d-flex flex-column justify-end align-center col-md-8 col-sm-6 col-12"
              >
                <div class="d-flex flex-row justify-center align-center mb-4">
                  <div class="px-4">
                    <b class=""> {{ following }}</b> <span>Following</span>
                  </div>
                  <div class="px-4">
                    <b class=""> {{ followers }}</b> <span>Followers</span>
                  </div>
                </div>
                <!-- <p>Other info about the profile here if there is any</p>-->
                <div>
                  <p
                    class="py-2 px-3 my-0 text-sm-body-2 text-md-body-1 card-user__description"
                  >
                    {{ description }}
                  </p>
                </div>
              </v-col>
            </v-row>
            <v-row> </v-row>
            <br />
            <v-divider></v-divider>

            <v-divider class="mx-16"></v-divider>
            <div>
              <v-row class="">
                <v-col>
                  <p class="px-6 my-0 mt-8 text-sm-body-2 text-md-body-1">
                    The following properties had the greatest effect on the
                    score. Positives increased the score, while negatives
                    decreased the score.
                  </p>
                </v-col>
              </v-row>
              <v-row
                class="px-3 d-flex justify-center mb-3 text-sm-body-2 text-md-body-1"
              >
                <v-col
                  align="center "
                  class="positive-container col-12 col-lg-6"
                >
                  <table class="table-positive">
                    <tr>
                      <th class="green-text font-weight-black">Positives</th>
                    </tr>
                    <tr>
                      <td class="table-data-positive">
                        <ul
                          v-for="(score, index) in scores.positives"
                          :key="index + 3"
                        >
                          <li>
                            <span
                              ><BIconCheck
                                style="width: 1.2rem; height: 1.2rem"
                                color="green"
                              ></BIconCheck></span
                            >{{ score.name }}
                          </li>
                          <li v-if="showPartial">
                            <span
                              ><BIconCheck
                                style="width: 1.2rem; height: 1.2rem"
                                color="green"
                              ></BIconCheck></span
                            >{{ score.contribution }}
                          </li>
                        </ul>
                      </td>
                    </tr>
                  </table>
                </v-col>

                <v-col
                  align="center"
                  class="positive-container col-12 col-lg-6"
                >
                  <table class="table-negative">
                    <tr>
                      <th class="red-text font-weight-black">Negatives</th>
                    </tr>
                    <tr>
                      <td class="table-data-negative">
                        <ul
                          v-for="(score, index) in scores.negatives"
                          :key="index + 3"
                        >
                          <li>
                            <span
                              ><BIconX
                                style="width: 1.2rem; height: 1.2rem"
                                color="#d70000"
                              ></BIconX></span
                            >{{ score.name }}
                          </li>
                          <li v-if="showPartial">
                            <span
                              ><BIconX
                                style="width: 1.2rem; height: 1.2rem"
                                color="#d70000"
                              ></BIconX></span
                            >{{ score.contribution }}
                          </li>
                        </ul>
                      </td>
                    </tr>
                  </table>
                </v-col>
              </v-row>
            </div>
          </v-card>
          <!-- Questionnaire is hidden for now  -->

          <!-- <div class="questionnaire-container bounce-animation">
            <a
              class="questionnaire_link"
              :href="feedbackLink"
              @click.prevent="feedbackClick"
            >
              <span class="questionnaire_header text-h6">Questionnaire</span>

              <div class="questionnaire_icon">
                <BIconArrowRightCircleFill></BIconArrowRightCircleFill>
              </div>
            </a>
          </div> -->
        </v-col>
        <!-- This Col is for the right container which includes the tweets from the API -->
        <v-col
          class="mt-6 positionRelative col-12 col-md-4 d-flex flex-column justify-center"
        >
          <div v-if="pinnedTweet">
            <h3 v-if="index == 0">Pinned</h3>
            <Tweet
              :id="pinnedTweet"
              :options="{ conversation: 'None', cards: 'hidden' }"
            ></Tweet>
          </div>
          <div v-for="(tweet, index) in tweets" :key="index">
            <Tweet
              :id="tweet"
              :options="{ conversation: 'None', cards: 'hidden' }"
            ></Tweet>
          </div>
          <div
            class="noTweetContainer"
            v-if="(!tweets || tweets.length == 0) && !pinnedTweet"
          >
            <h3>This user has no tweets. This may affect evaluation!</h3>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import "bootstrap-vue/dist/bootstrap-vue-icons.min.css";
import {
  // BIconArrowRightCircleFill,
  BIconCalendar3,
  // BIconAt,
  BIconGeoAlt,
  BIconCheck,
  BIconX,
} from "bootstrap-vue";
import { Tweet } from "vue-tweet-embed";
import Nav from "./Nav.vue";
export default {
  name: "ProfilePage",
  mounted() {},
  components: {
    Nav,
    // BIconArrowRightCircleFill,
    BIconCalendar3,
    BIconGeoAlt,
    // BIconAt,
    BIconCheck,
    BIconX,
    Tweet,
  },
  data() {
    return {
      apiUrl: process.env.VUE_APP_API_URL,
      profile: {},
      profile_pic_static: require("@/assets/profile_default.jpg"),
      showPartial: false,
      feedbackLink:
        "https://docs.google.com/forms/d/e/1FAIpQLScK4zOm5n0znSx1sM4Wg6wFG88FMqfjDvaN60vzV6NQVLNjTQ/viewform?usp=pp_url&entry.786300512=",
      userId: 0,
      requestOptions: {
        method: "POST",
        // mode: 'no-cors',
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true",
          "Access-Control-Allow-Headers":
            "Origin, X-Requested-With, Content-Type, Accept",
        },
        body: "",
      },
    };
  },
  methods: {
    listenForFocusFilterShortcut(event) {
      if (event.keyCode === 74 && event.altKey) {
        this.showPartial = !this.showPartial;
      }
    },
    feedbackClick() {
      console.log("CLICK");
      this.profile.userId = this.userId;
      this.requestOptions.body = JSON.stringify(this.profile);
      fetch(this.apiUrl + "SaveResults", this.requestOptions)
        .then((response) => {
          console.log(response);
          if (response.status == 201) window.open(this.feedbackLink, "_blank");
        })
        .catch((e) => {
          console.log("Error", e);
        });
    },
  },
  computed: {
    username() {
      return this.profile ? this.profile.name : "";
    },
    created_at() {
      const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      const createdDate = new Date(this.profile.created_at);
      // const createdDate = this.profile.created_at
      const month = months[createdDate.getMonth()];
      const year = createdDate.getFullYear();
      return `${month} ${year}`;
      // return this.profile ? this.profile.created_at : "";
    },

    description() {
      return this.profile ? this.profile.description : "";
    },
    location() {
      return this.profile ? this.profile.location : "";
    },
    profile_pic() {
      return this.profile
        ? this.profile.profile_image_url
        : this.profile_pic_static;
    },
    followers() {
      let number = this.profile
        ? this.profile.public_metrics.followers_count
        : 0;

      if (number >= 1000000000) {
        return (number / 1000000000).toFixed(0) + "B";
      } else if (number >= 1000000) {
        return (number / 1000000).toFixed(0) + "M";
      } else if (number >= 1000) {
        return (number / 1000).toFixed(0) + "K";
      } else {
        return number;
      }
    },
    following() {
      let number = this.profile
        ? this.profile.public_metrics.following_count
        : 0;
      if (number >= 1000000000) {
        return (number / 1000000000).toFixed(0) + "B";
      } else if (number >= 1000000) {
        return (number / 1000000).toFixed(0) + "M";
      } else if (number >= 1000) {
        return (number / 1000).toFixed(0) + "K";
      } else {
        return number;
      }
    },
    pinnedTweet() {
      return this.profile?.pinned_tweet_id
        ? this.profile?.pinned_tweet_id
        : null;
    },
    tweets() {
      let temp = [];
      if (this.profile?.tweets) {
        for (let i = 0; i < 3; i++) {
          if (this.profile.tweets[i]) temp.push(this.profile.tweets[i].id);
        }
      }
      return temp;
    },
    scores() {
      return this.profile?.ml_output
        ? {
            ...this.profile.ml_output.explanations,
            score: this.profile.ml_output.score,
          }
        : { score: 0 };
    },
  },
  created() {
    this.profile = this.$store.state.profile;
    if (Object.keys(this.profile).length === 0) {
      this.$router.push({ name: "Main" });
    }
    this.userId = new Date().getTime();
    this.feedbackLink = this.feedbackLink + this.userId;
    window.addEventListener("keyup", this.listenForFocusFilterShortcut);
  },
  beforeDestroy() {
    window.removeEventListener("keyup", this.listenForFocusFilterShortcut);
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Kanit&family=Orbitron:wght@600&family=Unbounded&display=swap");
.font-custom {
  font-family: "Kanit", sans-serif;
  font-family: "Orbitron", sans-serif;
  font-family: "Unbounded", cursive;
}
.btn-back {
  font-family: "Kanit", sans-serif;
  font-family: "Orbitron", sans-serif;
  font-family: "Unbounded", cursive;
  background-color: #6a9ad2;
  color: black;
}

.profile-pic {
  border-radius: 50%;
}

.green-text {
  color: green;
}
.red-text {
  color: #d70000;
}

.card__header {
  background: #264391;
  color: white;
  align-items: center;
  box-shadow: rgba(0, 0, 0, 0.35) 0px -50px 36px -28px inset;
  border-radius: 0.55rem;
}
.circle {
  border-radius: 100%;
  height: 3.3rem;
  width: 3.3rem;
  display: flex;
  box-shadow: 0 2px 5px 1px rgb(124, 124, 124);
  align-items: center;
  border: 3px solid #517aba;
  justify-content: center;
  margin: 0.25rem;
  padding: 0.5rem;
}
.card__score-col-circle {
  border-radius: 100%;
  height: 4.5rem;
  width: 4.5rem;
  display: flex;
  align-items: center;
  border: 5px solid #ffffff;
  justify-content: center;
  margin-left: 0.5rem;
}

.stats {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.nlp-results-container {
  display: flex;
  align-items: center;
}
.positive-container,
.negative-container {
  width: 100% !important;
}

th {
  padding: 0.625rem;
  border-bottom: 1px #e1e1e1 solid;
}
td {
  padding: 1rem;
}

ul {
  padding-left: 0 !important;
}
li {
  text-align: left;
  list-style: none;
}
table {
  align-items: center;
  justify-content: center;
  align-content: center;
  min-width: 100% !important;
  background-color: transparent;
  border: 1px solid #e1e1e1;
  border-top: 5px solid #1f3778;
  border-top-right-radius: 0.555rem;
}

.questionnaire-container {
  border: dashed 3px rgb(227, 107, 1);
  border-radius: 2rem;
  text-decoration: none;
  position: fixed;
  right: 5%;
  bottom: 5%;
  font-size: 1.5rem;
  padding: 0.3rem;
  z-index: 100;
  background-color: rgba(183, 183, 183, 0.6);
}

.bounce-animation {
  animation: bounce 3s ease infinite;
}
@keyframes bounce {
  30% {
    transform: scale(1);
  }
  40%,
  60% {
    transform: rotate(-6deg) scale(1);
  }
  50% {
    transform: rotate(6deg) scale(1);
  }
  70% {
    transform: rotate(0deg) scale(1);
  }
  100% {
    transform: scale(1);
  }
}

.questionnaire-container a {
  color: black !important;
  text-decoration: none;
}
.questionnaire_icon {
  background-color: rgb(227, 107, 1);
  border-radius: 50%;
  width: 50px;
  height: 50px;
  align-items: center;
  justify-content: center;
  display: flex;
  color: white;
}
.questionnaire_link {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}
.questionnaire_header {
  padding: 0 0.75rem;
}

@media only screen and (max-width: 960px) {
  .nav_logo {
    padding-right: 0.1rem;
  }
  .questionnaire-container {
    border: dashed 2px rgb(227, 107, 1);
    position: fixed;
    right: 2%;
    bottom: 2%;
    font-size: 0.8rem;
    padding: 0.3rem;
  }
  .questionnaire_icon {
    width: 30px;
    height: 30px;
  }
  .questionnaire_header {
    padding: 5px;
    font-size: 1rem !important;
  }
}
.card-pic_username {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.card-pic_username p {
  padding: 0;
  margin: 0;
}

.locationUsername {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.card__score-col {
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.card__score-col-container p {
  padding: 0;
  margin: 0;
}

.card-user__description {
  text-align: left;
}

.displayFlex {
  display: flex;

  justify-content: space-between;
  flex-direction: row;
  flex: 1 0 auto;
}
.noTweetContainer {
  color: #793261;
  position: absolute;
  top: 50%;
  right: 50%;
  transform: translate(50%, 50%);
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.positionRelative {
  position: relative;
}
</style>
