# starpastoral/Dexter

⭐ 10 · Rust · 推送 2026-02-08 · [GitHub](https://github.com/starpastoral/Dexter) · 个人维护

**终端 AI 命令助手：把自然语言路由到 CLI 工具并执行**

基于 Rust/ratatui 的终端 TUI 应用：用路由模型把自然语言请求分配到 f2、ffmpeg、pandoc、qpdf、ocrmypdf、yt-dlp、whisper-cpp、jdupes、libvips 等插件适配的 CLI 工具，生成命令并经确认后执行。支持多家 LLM 提供商配置与多模型 fallback 顺序、首次运行引导式设置、高风险命令拦截与显式确认流程。依赖 Rust 工具链与 PATH 中的相关 CLI 工具，通过 install.sh 或 cargo build 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 路由模型为请求选择插件，多提供商/多模型 fallback 排序
- 确认优先执行：高风险命令拦截、无确认不执行
- 集成 9 类 CLI 工具的命令构建（重命名/媒体/下载/PDF/OCR/转录/去重/图像）
- ratatui 主题化终端 UI 与引导式设置向导

## 适用场景

- 用自然语言批量重命名文件并让 AI 生成 f2 命令
- 把 YouTube 视频下载为 mp3 等媒体处理任务
- 本地语音转录、OCR PDF、图片批处理等 CLI 工作流的对话式操作

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: Dexter is a terminal-based AI assistant that routes natural-language intent to specialized CLI tools (such as `f2`, 
> L9: - **Intelligent Routing**: A router model selects the most suitable plugin for each request.

## 星数曲线

```mermaid
xychart-beta
    title "starpastoral/Dexter 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `d43e8c2a20a1` · [字段定义](../../DATASET.md)*
