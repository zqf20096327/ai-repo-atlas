# saltysalrua/Novelai-harness

⭐ 25 · Dart · MIT · 推送 2026-11-26 · [GitHub](https://github.com/saltysalrua/Novelai-harness) · 个人维护 · 中文 README

**NovelAI 第三方跨平台客户端与 AI 对话工作台**

基于 Flutter 的非官方 NovelAI 客户端，覆盖 Windows、macOS、Linux 和 Android。图像侧适配 NovelAI Diffusion V5/V4.5/V4/V3 与 Furry 系列模型，支持精准参考、Vibe Transfer、多角色定位、局部重绘、Anlas 消耗计算与 429 重试；也可通过 PromptToolkit AI Bridge 连接本地 ComfyUI。对话侧支持 OpenAI 兼容、Anthropic Messages、Google Gemini 接口，AI 可调用工作台工具修改生图参数、发起生图或重绘。内置 Danbooru 离线标签库、PNG 元数据回填与水印功能。需自备 NovelAI 账号，API 费用由用户承担。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 适配 NovelAI V5/V4.5/V4/V3 及 Furry 系列生图模型
- AI 对话中直接调用工作台工具（改参、生图、重绘、词库检索）
- 内置 Danbooru 离线标签库与 T5/Qwen Token 计数
- 可选基于 Cloudflare Workers + D1 的词库云同步

## 适用场景

- 在桌面或安卓设备上使用 NovelAI 生图并管理参数与历史
- 通过对话让 AI 直接调整生图参数并发起重绘
- 离线补全 Danbooru 标签并整理复用提示词组合
- 连接本地 ComfyUI 进行参数下发与生图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: 基于 Flutter 的 NovelAI 第三方跨平台客户端与 AI 对话工作台，支持 Windows、macOS、Linux 和 Android。
> L20: - **NovelAI 协议适配**：支持 NovelAI Diffusion V5 / V4.5 / V4 / V3 及 Furry 系列模型，提供 2D 分辨率面板、采样器与调度器配置、单并发排队和 429 重试。
> L26: - **多协议 LLM 接入**：支持 OpenAI 兼容、Anthropic Messages 和 Google Gemini Interactions 接口，支持流式输出、思考强度切换、多模态图片发送与上下文压缩。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `2eb7348e1bbd` · [字段定义](../../DATASET.md)*
