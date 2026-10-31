# jeremieLouvaert/ComfyUI-Higgsfield-Direct

⭐ 14 · Python · MIT · 推送 2026-08-15 · [GitHub](https://github.com/jeremieLouvaert/ComfyUI-Higgsfield-Direct) · 个人维护

**ComfyUI 节点包：直连 Higgsfield API 生成图像与视频**

面向 ComfyUI 用户的自定义节点包，通过用户自有 Higgsfield API key 直接调用 100+ 生成模型，提供文生图（Soul 2.0、Seedream 4、Reve）、图像编辑（Seedream 4 Edit）、图生视频（Kling 2.1、Seedance、DOP）四类节点，输出原生 ComfyUI VIDEO 类型并自动保存到输出目录。无积分系统，按次计费；支持 1K/2K/4K 分辨率与多种宽高比。安装方式为克隆到 custom_nodes 并安装依赖，API key 支持文件、环境变量、节点输入三种配置。限制：生成文件在 Higgsfield 侧仅保留至少 7 天，需依赖本地自动下载留存。

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

- 单一节点包接入 Higgsfield 100+ 生成模型
- 文生图/图像编辑/图生视频三类生成节点，视频输出原生 ComfyUI VIDEO 类型
- 生成结果自动下载到 ComfyUI 输出目录，规避远端 URL 失效
- API key 支持文件/环境变量/节点字段三种配置方式

## 适用场景

- 在 ComfyUI 工作流中调用 Higgsfield 的图像与视频模型
- 用参考图保持风格/角色一致性（Soul ID）
- 生成 5-15 秒短视频并接入 ComfyUI 视频处理链路

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: **Direct Higgsfield API integration for ComfyUI**, unified access to 100+ generative models through a single node pa
> L13: |**Higgsfield Text-to-Image**|Generate images from text prompts (Soul, Seedream 4, Reve)|
> L15: |**Higgsfield Image-to-Video**|Convert images to video (Kling 2.1, Seedance, DOP), returns a native ComfyUI `VIDEO`

## 星数曲线

```mermaid
xychart-beta
    title "jeremieLouvaert/ComfyUI-Higgsfield-Direct 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c151229ab289` · [字段定义](../../DATASET.md)*
