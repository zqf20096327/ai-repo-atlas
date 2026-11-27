# mousebomb/mbai-platform

⭐ 4 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/mousebomb/mbai-platform) · 个人维护 · 中文 README

**本地自托管多模态 AI 能力平台，提供统一 REST/MCP 接口**

以 ComfyUI 为模型运行时、自身只做控制平面（能力注册表、统一队列、产物库、引擎适配器）的本地平台，聚合图片生成/改图/抠图/超分/立绘拆层、语音合成/音色克隆/音色设计/语音转写、图生视频共 12 项能力 24 个变体，并有 9 项明确标「未接」。对外提供网页界面、REST API、MCP 服务与 OpenAI 兼容端点（仅两条），供本地智能体或现成客户端调用。单卡 RTX 3060 12GB / Windows 实测跑通，音频引擎为可选安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 项能力 / 24 个变体，产物覆盖图片、视频、音频、文本、PSD/ZIP 五种形态
- 统一 REST 接口 + MCP 服务 + OpenAI 兼容端点（speech / images generations 两条）
- 能力矩阵按成熟度 L0~L3 公开，未接能力明确标注
- 模型文件经 profiles/local.yaml 本机映射，换模型版本不改代码

## 适用场景

- 在本地 12GB 显存的 Windows 机器上跑生图、TTS、抠图等 AI 能力
- 让 Claude Desktop / opencode 等客户端的 Agent 通过 MCP 提交生成任务
- 给 Cherry Studio / Dify / LangChain 等现成 OpenAI 客户端配 base_url 使用本地模型

## 场景标签

`图像生成` `语音合成` `视频生成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L12: **一站式本地 AI 能力平台**：生图 / 改图 / 蒙版重绘 / 抠图 / 超分 / 立绘拆层 / 图生视频 /
> L13: 语音合成 / 音色克隆 / 音色设计 / 语音转写，一套 REST 接口 + 一个网页 + 一个 MCP 服务交给本地智能体调用。
> L26: 设计原则：**不自研推理内核**。ComfyUI 当模型运行时，平台只做控制平面（能力注册表、统一队列、产物库、引擎适配器）。

## 星数曲线

```mermaid
xychart-beta
    title "mousebomb/mbai-platform 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-26", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `b4ebeec7ce1a` · [字段定义](../../DATASET.md)*
