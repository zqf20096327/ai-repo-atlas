# rwightman/gemma4_pytorch_claude

⭐ 15 · Python · Apache-2.0 · 推送 2026-07-26 · [GitHub](https://github.com/rwightman/gemma4_pytorch_claude) · 个人维护

**Gemma 4 全家族的独立 PyTorch 实现，支持文本/视觉/音频**

Google Gemma 4 模型家族的独立 PyTorch 复现库，从官方 JAX 参考逐层移植并对每个模块做数值验证（最大绝对误差 1e-05 量级）。覆盖 E2B/E4B/12B/31B/26B-A4B 五个变体，含 GQA、滑动窗口+全局注意力、PLI、KV 共享、MoE 与 12B 的无编码器多模态（原始像素块与波形直接投影）。提供 Composer 多模态入口、chat/generate/批流式生成、KV 缓存管理（32k 上下文下 31B 缓存可从 29.5GB 降至 3.5GB）、HuggingFace safetensors 加载与 JAX 检查点转换 CLI，附带约 265 个测试。面向需要研究或二次开发 Gemma 4 内部实现的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个 Gemma 4 变体（E2B 至 26B-A4B MoE），文本/视觉/音频三模态
- 逐模块对照 JAX 参考做数值验证，附误差表
- 12B 变体无编码器：48×48 原始像素块与 16kHz 波形帧直接投影进文本空间
- KV 缓存按滑动窗口分层分配，长上下文显存占用大幅降低

## 适用场景

- 加载 HuggingFace 权重做 Gemma 4 文本生成、图像描述或音频转录
- 研究 Gemma 4 架构细节（GQA/PLI/KV 共享/MoE）并做修改实验
- 把 JAX/Orbax 检查点转换为 safetensors 格式

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: A clean, standalone PyTorch implementation of Google's **Gemma 4** model family — ported layer-by-layer from the off
> L104: For instruction-tuned checkpoints, prefer `chat()` for single-turn prompts:

## 星数曲线

```mermaid
xychart-beta
    title "rwightman/gemma4_pytorch_claude 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c0434cb22598` · [字段定义](../../DATASET.md)*
