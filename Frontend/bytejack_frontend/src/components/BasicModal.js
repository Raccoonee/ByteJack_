import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid darkred',
  boxShadow: 24,
  p: 4,
};

const textStyle = {
  textAlign: 'center',
  fontWeight: 'bold',
  color: 'darkred',
};


export default function BasicModal({setOpen, open}) {
  return (
    <div>
      <Modal
        open={open}
        onClose={() => {setOpen(false)}}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography sx={textStyle} id="modal-modal-title" variant="h4" component="h2">
            Incorrect Login Information
          </Typography>
        </Box>
      </Modal>
    </div>
  );
}
