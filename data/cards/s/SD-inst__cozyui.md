# SD-inst/cozyui

⭐ 16 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/SD-inst/cozyui) · 个人维护

**ComfyUI 的前端界面：更简便地生成 AI 图像/视频/音频**

基于 TypeScript/React/MaterialUI 的 ComfyUI 替代前端，界面设计参考 AUTOMATIC1111 Web UI 并支持移动端。支持 T2I/T2V/I2V/V2V、文本转音频、TTS、音乐生成等多种模型（Hunyuan、Wan 2.1、LTX、MiniMax H3、Flux、Qwen Image、SD 等），附 LLM 提示词助手（OpenAI 兼容 API）、历史/预设/会话的浏览器本地存储（IndexedDB）、LoRA 权重合并、VRAM 优化（TeaCache/MultiGPU）。构建需 Yarn 4 并连接运行中的 ComfyUI，提供 NVIDIA-only Docker Compose 方案。明确非目标：不做 ComfyUI 替代品、无插件系统。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 T2I/T2V/I2V/V2V/T2A/TTS/音乐等多类生成模式与众多模型
- LLM 提示词助手：OpenAI 兼容 API、视觉输入、会话持久化
- 历史/预设/会话存储于浏览器 IndexedDB，支持导入导出
- Docker Compose 一键部署 ComfyUI+CozyUI（NVIDIA）

## 适用场景

- 想要比 ComfyUI 原生界面更简便的生成界面
- 在手机或平板上进行文生图/文生视频操作
- 管理生成历史、对比两次生成结果的差异

## 场景标签

`图像生成` `视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: This is a yet another frontend for ComfyUI to make it actually not so painful to use. It's designed after AUTOMATIC1
> L114: - ComfyUI replacement

## 星数曲线

```mermaid
xychart-beta
    title "SD-inst/cozyui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `97e1925f948a` · [字段定义](../../DATASET.md)*
