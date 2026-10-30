# aigem/comfyui_gemini_nano_banana

⭐ 59 · Python · MIT · 推送 2025-12-14 · [GitHub](https://github.com/aigem/comfyui_gemini_nano_banana) · [官网](https://github.com/aigem/ComfyUI_KuAi_Power) · 组织维护 · 中文 README

**ComfyUI 节点：通过 Gemini 兼容 API 做自然语言改图**

面向 ComfyUI 的自定义节点，将输入图像与自然语言指令发送至 Gemini 2.5 Flash Image（兼容 API，支持自定义 Base URL，默认 kuai.host）进行图像编辑，输出图像张量与含延迟、重试、token 用量的 metrics_json。提供指令预设与系统提示词机制、最多 4 张参考图、temperature/top_p 等参数，及 429/5xx 指数退避重试。安装方式为克隆仓库到 custom_nodes 并安装依赖。README 首行声明已迁移至新仓库，本仓库不再更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 Gemini 2.5 Flash Image 兼容 API（可自定义 Base URL）进行图像编辑
- 输出 metrics_json：延迟、重试次数、请求次数、token 使用指标
- instruction_presets 指令预设与 Markdown 系统提示词机制
- 最多 4 张参考图融合与 429/5xx 指数退避重试

## 适用场景

- 在 ComfyUI 工作流中用自然语言指令编辑图像
- 通过参考图融合角色或道具细节
- 需要记录 API 调用指标的图像编辑流程

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L14: 一个面向生产的 ComfyUI 节点，使用 Gemini 2.5 Flash Image（兼容 API）对输入图像进行编辑。将本项目放入 `ComfyUI/custom_nodes/` 后，即可在 ComfyUI 中用自然语言指令
> L22: 1. 复制或克隆本仓库到 `ComfyUI/custom_nodes/confyui-gemini-nano-banana`。
> L88: - 节点调用端点：`{base_url}/v1beta/models/{model}:generateContent`（默认 base_url 为 `https://apis.kuai.host/`）

## 星数曲线

```mermaid
xychart-beta
    title "aigem/comfyui_gemini_nano_banana 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-30 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3115680458cd` · [字段定义](../../DATASET.md)*
