# OnlyTerp/kvtc

⭐ 24 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/OnlyTerp/kvtc) · 个人维护

**NVIDIA KVTC 首个开源实现：PCA+自适应量化+熵编码压缩 LLM KV 缓存**

KV 缓存张量压缩库，复现 NVIDIA 论文（arXiv 2511.01815, ICLR 2026）。三阶段流水线：RoPE 逆变换后做 PCA 去相关、动态规划在总位预算下分配各分量位宽（0 位即剪枝）、DEFLATE/LZMA2 熵编码二选一。另含非对称 K/V 位宽、attention sink 与滑窗 FP16 保护等机制。README 报告 6-9x 压缩（V 余弦 0.996 @6x），需 CUDA GPU 与每模型一次性校准（约 10 条文本）。以源码 pip install -e 方式安装，附 Colab 演示与基准脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段流水线：RoPE 逆变换 + PCA + DP 位分配 + DEFLATE/LZMA2 熵编码
- 非对称 K/V 位宽、attention sink 与滑窗 FP16 保护
- README 报告 6-9x 压缩，Qwen2.5-7B 上 V 余弦相似度 0.996 @5.9x
- 每模型一次性校准（约 10 条文本）生成 PCA 基

## 适用场景

- 长上下文推理时压缩 KV 缓存以降低显存占用
- 在单卡上运行更长上下文（README 称 RTX 5090 跑 2M+ token）
- 对比研究 KV 缓存压缩方法的质量-压缩比权衡

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: **The first open-source implementation of NVIDIA's KVTC (arXiv 2511.01815, ICLR 2026)**
> L19: Every token an LLM generates stores key-value pairs across every attention layer. This **KV cache** grows linearly 
> L60: KVTC applies **media-compression techniques** (the same ideas behind JPEG and H.264) to KV cache vectors. The pipel

## 星数曲线

```mermaid
xychart-beta
    title "OnlyTerp/kvtc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5f6990917157` · [字段定义](../../DATASET.md)*
