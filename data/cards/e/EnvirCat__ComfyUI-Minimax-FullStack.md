# EnvirCat/ComfyUI-Minimax-FullStack

⭐ — · [GitHub]() · 个人维护 · 中文 README

**ComfyUI 一站式 MiniMax H3 视频生成节点包**

以 ComfyUI 自定义节点形式提供的 H3 视频创作工作流：串联参考素材管理、可选参考图生成、意图到提示词设计、视频/音频生成、预览、插帧、放大与导出，可一键运行或在图像与提示词检查点暂停编辑。核心机制是参考感知的意图提示：本地视觉语言模型阅读素材并按 MiniMax 官方提示词结构生成 H3 提示词，也可切换 OpenAI 兼容 API 后端；远程图像分析需显式开启，API key 不序列化进工作流。安装需置于 ComfyUI/custom_nodes 并补装上游节点与权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地视觉语言模型按 MiniMax 官方规范生成 H3 结构化提示词
- 参考图生成、视频 LoRA、插帧（RIFE）、Lanczos 放大与导出集成于一个工作区
- 中英双语 UI，支持一键运行或分段暂停审阅
- 附 221 项 Python 测试与 86 项前端测试

## 适用场景

- 在 ComfyUI 中从意图和有序参考素材生成 H3 视频
- 用本地多模态模型替代 API 做提示词设计
- 对参考图、LoRA、提示词分段检查后再生成视频

## 场景标签

`视频生成` `图像生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: MiniMax H3 Full Stack combines reference management, optional reference-image generation, intent-to-prompt design, H
> L9: Its central feature is **reference-aware intent prompting**: describe what you want, and a local vision-language mod
> L26: 1. Install into `ComfyUI/custom_nodes/ComfyUI-Minimax-FullStack`, install Python requirements **with ComfyUI's Pyth

## 星数曲线

```mermaid
xychart-beta
    title "EnvirCat/ComfyUI-Minimax-FullStack 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-20 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a3039d44dccb` · [字段定义](../../DATASET.md)*
