import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import PropTypes from "prop-types";
import React from "react";
import { connect } from "react-redux";
import { getProfile } from "redux/actions/profile";
import ProfileHeader from "./ProfileHeader";
import ProfileInformation from "./ProfileInformation";
import WorkArea from "./WorkArea";

const ProfileDetail = (props) => {
  return (
    <>
      <Container>
        <Stack spacing={3}>
          <ProfileHeader profile={props.profile} />
          <Grid container spacing={2}>
            <Grid item xs={12} md={8}>
              <ProfileInformation profile={props.profile} />
            </Grid>
            <Grid item xs={12} md={4}>
              <Box>
                <WorkArea profile={props.profile} />
              </Box>
            </Grid>
          </Grid>
        </Stack>
      </Container>
    </>
  );
};

ProfileDetail.propTypes = {
  isAuthenticated: PropTypes.bool.isRequired,
  loading: PropTypes.bool.isRequired,
  profile: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
  profile: state.profile.profile,
  loading: state.profile.loading,
});

export default connect(mapStateToProps, { getProfile })(ProfileDetail);
