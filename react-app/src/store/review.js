const GET_REVIEWS = 'reviews/GET_REVIEWS';
const ADD_REVIEW = 'reviews/ADD_REVIEW';

const getReviews = (reviews) => ({
  type: GET_REVIEWS,
  payload: reviews
})

const addReview = (data)

export const getReviewsThunk = () => async (dispatch) => {
  const response = await fetch('/api/reviews');
  if (response.ok) {
    const data = await response.json()
    if (data.errors) {
      return data.errors;
    }
    dispatch(getReviews(data));
  }
}

const initialState = {}

export default function review_reducer(state = initialState, action) {
  switch (action.type) {
    case GET_REVIEWS:
      let newState = {}
      action.payload.reviews.forEach((review) => {
        newState[review.id] = review;
      })
      return newState;
    default:
      return state
  }
}
