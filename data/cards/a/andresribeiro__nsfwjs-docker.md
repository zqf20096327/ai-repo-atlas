# andresribeiro/nsfwjs-docker

⭐ 98 · TypeScript · MIT · 推送 2026-05-24 · [GitHub](https://github.com/andresribeiro/nsfwjs-docker) · [官网](https://hub.docker.com/r/andresribeiroo/nsfwjs) · 个人维护

**自托管 NSFW 图片检测 API，Docker 一行命令部署**

基于 NSFWJS 模型封装的 Docker 化图像内容审核服务：接收 JPEG/PNG/WebP/AVIF/TIFF/GIF（首帧）及原始像素数据，输出 Neutral/Drawing/Sexy/Hentai/Porn 五类概率分类。服务端用 Deno + Hono 框架实现，sharp/libvips 做 SIMD 加速的图像解码与缩放，jemalloc 优化并发内存使用，推理失败时自动释放 TensorFlow 张量防止内存泄漏。镜像支持 x64 与 arm64，运行内存低于 350MB，端口 3333，可通过 docker run 或从源码构建部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五类 NSFW 分类输出，每类概率 0-1
- 支持 JPEG/PNG/WebP/AVIF/TIFF/GIF/原始像素输入
- 多架构镜像（x64/arm64），运行内存低于 350MB
- sharp SIMD 加速解码与 jemalloc 内存分配器

## 适用场景

- 给 UGC 平台接入图片内容审核接口
- 自托管方式处理敏感图像分类，不依赖第三方 API
- 在 x64 或 arm64 服务器上低资源部署检测服务

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: High-performance, self-hosted NSFW detection API powered by
> L13: - **Output:** 5-class classification — Neutral, Drawing, Sexy, Hentai, Porn;

## 星数曲线

```mermaid
xychart-beta
    title "andresribeiro/nsfwjs-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-28 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fae56da7e192` · [字段定义](../../DATASET.md)*
