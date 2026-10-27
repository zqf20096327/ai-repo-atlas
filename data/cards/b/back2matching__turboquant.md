# back2matching/turboquant

⭐ 46 · Python · NOASSERTION · 推送 2026-10-07 · [GitHub](https://github.com/back2matching/turboquant) · [官网](https://pypi.org/project/turboquant/) · 个人维护

**LLM 推理 KV cache 压缩库：4-bit 量化省 VRAM、兼容 HuggingFace**

实现 Google TurboQuant 算法（ICLR 2026）的 Python 库，将 LLM 推理时的 KV cache 从 FP16 压缩到 3-4 bit：随机旋转 + 解析式最优码本 + 128 token 残差窗口，无需训练数据与校准，即装即用。可 drop-in 到任意 HuggingFace 模型，附带 OpenAI 兼容推理服务器（turboquant-server）与直接量化向量的核心 API。README 提供多模型 RTX 4080 基准：VRAM 节省随上下文增长（4K 约 1GB、8K 约 2GB），短上下文时吞吐可能低于 FP16，StableLM 上反而更耗 VRAM。限制：3-bit 对小模型质量下降明显，混合架构（Mamba 等）不适用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- KV cache 4-bit 量化，无需校准即可用于任意 HuggingFace 模型
- 附带 OpenAI 兼容推理服务器 turboquant-server
- 非对称 K/V 分配与层自适应精度（首末层保持 FP16）
- 提供 RTX 4080 上 4 个模型的 VRAM/吞吐基准数据与复现脚本

## 适用场景

- 在 16GB 级 GPU 上跑 8K+ 长上下文推理
- 多用户服务时在显存中装下更多 KV cache
- 腾出 KV cache 显存以运行更大模型

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L11: Drop-in for any HuggingFace model:
> L28: TurboQuant compresses the cache to 4 bits (from 16) using Google's TurboQuant algorithm (ICLR 2026). No training da

## 星数曲线

```mermaid
xychart-beta
    title "back2matching/turboquant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-27 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `54b0cad1bab3` · [字段定义](../../DATASET.md)*
