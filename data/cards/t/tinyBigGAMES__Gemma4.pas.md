# tinyBigGAMES/Gemma4.pas

⭐ 32 · Python · NOASSERTION · 推送 2026-07-08 · [GitHub](https://github.com/tinyBigGAMES/Gemma4.pas) · 组织维护

**纯 Delphi 编写的 Gemma 4 E4B 本地多模态推理引擎**

用 Delphi 实现的本地推理引擎，在 Windows x64 上经 Vulkan compute shader 运行 Google Gemma 4 E4B（Q4_0 量化，SigLIP 视觉、Conformer 音频、视频帧采样），并附带 EmbeddingGemma-300m 嵌入模型支持语义检索与 RAG。零第三方依赖，单一 VPK 归档装载双模型。可选应用层提供工具调用、SQLite+FTS5+HNSW 持久记忆、会话循环与控制台聊天。需 Delphi 12 Athens 编译，限定 NVIDIA Vulkan GPU（RTX 3060 12GB 实测约 57 tokens/sec）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Delphi 实现，无 Python/C++/DLL 依赖，Vulkan SPIR-V 着色器执行矩阵运算
- 文本/视觉/音频/视频多模态生成，含 thinking 推理通道与流式输出
- 附带 EmbeddingGemma-300m（768 维）支持语义检索与 RAG
- 可选应用层：工具注册、SQLite+FTS5+HNSW 持久记忆、KV 缓存保存恢复

## 适用场景

- Delphi/Pascal 开发者在应用内集成本地 LLM 推理
- 需要全离线、无遥测的本地多模态 AI 能力
- 构建带工具调用与持久记忆的本地对话助手

## 场景标签

`推理引擎` `多模态` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L7: **A complete multimodal AI inference engine for Google's Gemma 4 E4B, written entirely in Delphi.** No Python, no C/
> L16: Gemma4.pas runs the full Gemma 4 E4B model: text generation with a thinking/reasoning channel, vision, audio, and v

## 星数曲线

```mermaid
xychart-beta
    title "tinyBigGAMES/Gemma4.pas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d79ed94e08c5` · [字段定义](../../DATASET.md)*
