# ZhouXiaolin/opencat

⭐ 71 · Rust · 推送 2026-10-22 · [GitHub](https://github.com/ZhouXiaolin/opencat) · [官网](http://www.catcut.cc) · 个人维护 · 中文 README

**面向 AI agent 的 JSX 声明式视频渲染引擎（Rust+Skia+FFmpeg）**

用 JSX 定义场景、动画与布局，Rust 侧经 Taffy 布局、Skia GPU 渲染、FFmpeg 编码，一条命令输出 MP4；确定性渲染，跨机器结果一致，无需浏览器或 Chromium 快照。提供 GSAP 兼容声明式动画 API、多场景时间线与转场、Tailwind 风格布局、音频混流、字幕引擎，以及 WASM+CanvasKit 的浏览器端渲染管线（opencat-web，无需服务器）。定位服务 AI 视频流水线：模型输出 JSX，引擎负责渲染。需从源码用 Cargo 构建，依赖 Rust nightly、FFmpeg 6.x 开发库，Linux 另需 OpenGL/EGL 与 Fontconfig 开发库，Windows 构建需配置两个链接器 flag。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JSX 声明式定义视频，cargo run 一条命令出 MP4
- 双渲染管线：Rust(GPU)+FFmpeg 与 WASM+CanvasKit（浏览器端免服务器）
- GSAP 兼容动画 API（80%+ 覆盖）、多场景时间线与内置转场效果
- 确定性渲染：value = f(time)，跨机器一致，像素级对齐校验工具 k3diff

## 适用场景

- AI agent 生成 JSX 后自动渲染成视频，接入视频流水线
- 在浏览器内做视频渲染/编辑，无需后端服务器
- 程序化动画与批量视频生产：换 props 即换一支视频

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L326: - **AI video pipelines**: model outputs JSX, engine renders video, lowest integration cost
> L17: JSX defines scenes, animations, and layouts. Skia GPU renders, FFmpeg encodes to MP4 — deterministic, cross-platfor

## 星数曲线

```mermaid
xychart-beta
    title "ZhouXiaolin/opencat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-24 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e0d6ea641cc7` · [字段定义](../../DATASET.md)*
