<template>
    <div class="container-fluid text-center p-4">
        <div class="row">
            <!-- Kiri -->
            <div class="col-3 border-end border-1 border-danger" style="padding-right: 0">
                <div class="border-bottom border-2 border-danger" style="height: 6rem">Jacob's Breakfast</div>
                <div class="border-bottom border-2 border-danger overflow-scroll" style="height: 24rem">Invoice Body</div>
                <div class="" style="height: 6rem">Commands</div>
            </div>

            <!-- Kanan -->
            <div class="col-9 border-start border-1 border-danger">
                <!-- Content -->
                <div class="row" style="height: 478px">
                    <!-- Category Tab -->
                    <nav>
                        <div class="nav nav-tabs" id="nav-tab" role="tablist">
                            <button class="nav-link active" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home" type="button" role="tab" aria-controls="nav-home" aria-selected="true">Appetizer</button>
                            <button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Main Course</button>
                            <button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Dessert</button>
                            <button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Soup</button>
                            <button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button" role="tab" aria-controls="nav-profile" aria-selected="false">Drink</button>
                            <button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Others</button>
                        </div>
                    </nav>

                    <!-- Isi category -->
                    <div class="tab-content pt-3" id="nav-tabContent">
                        <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab" tabindex="0">
                            <div class="row row-cols-1 row-cols-md-3 g-4">
                                <div class="col">
                                    <div class="card h-100">
                                        <img src="..." class="card-img-top" alt="Alt-Image" />
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="col">
                                    <div class="card h-100">
                                        <img src="..." class="card-img-top" alt="Alt-Image" />
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="col">
                                    <div class="card h-100">
                                        <img src="..." class="card-img-top" alt="Alt-Image" />
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="col">
                                    <div class="card h-100">
                                        <img src="..." class="card-img-top" alt="Alt-Image" />
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="col">
                                    <div class="card h-100">
                                        <img src="..." class="card-img-top" alt="Alt-Image" />
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                        </div>
                                    </div>
                                </div>

                                <div class="col">
                                    <div class="card h-100">
                                        <img src="..." class="card-img-top" alt="Alt-Image" />
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab" tabindex="0">...</div>
                        <div class="tab-pane fade" id="nav-contact" role="tabpanel" aria-labelledby="nav-contact-tab" tabindex="0">...</div>
                        <div class="tab-pane fade" id="nav-disabled" role="tabpanel" aria-labelledby="nav-disabled-tab" tabindex="0">...</div>
                    </div>
                </div>

                <!-- Report Sale -->
                <div class="row border-top border-2 border-danger">
                    <h1>Report Sale</h1>
                </div>
            </div>
        </div>
    </div>
</template>
