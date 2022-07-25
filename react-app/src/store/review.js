const GET_REVIEWS = 'reviews/GET_REVIEWS'

const getReviews = (reviews) => ({
  type: GET_REVIEWS,
  reviews
})

export const getReviewsThunk = () => async (dispatch) => {
  const response = await fetch('/')
}
