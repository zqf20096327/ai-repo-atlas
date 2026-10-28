# kevbuh/bitnet

⭐ 32 · Python · 推送 2026-03-26 · [GitHub](https://github.com/kevbuh/bitnet) · 个人维护

**微软 BitNet b1.58 2B4T 的纯 PyTorch 复现实现**

用 PyTorch 实现 Microsoft BitNet b1.58 2B4T 模型架构：三值权重 STE、逐 token 8-bit abs-max 激活量化、SubLN、ReLU² FFN、RoPE/GQA 注意力，2.4B 参数。README 给出 HF 风格的 config（BitNetForCausalLM、auto_map 指向自定义 modeling/configuration 代码）以及逐层权重形状与参数量统计（共 2,412,820,480 参数）。安装方式为 source setup.sh 脚本；README 中未见推理或使用示例，文档以配置与层信息罗列为主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三值权重 [1,0,-1] 的 BitNet 架构 PyTorch 实现
- 提供 HF transformers 兼容的 config 与 auto_map 自定义代码入口
- 列出全部 2,412,820,480 参数的逐层形状统计

## 适用场景

- 研究 BitNet 1.58bit 量化架构的实现细节
- 在自定义 PyTorch 代码中加载/复现 bitnet-b1.58-2B-4T 模型

## 场景标签

 · 领域:机器学习/模型实现

## 证据(README 行号)

> L1: # bitnet
> L3: ```bitnet``` is based on Microsoft's [BitNet b1.58 2B4T](https://huggingface.co/microsoft/bitnet-b1.58-2B-4T), a bin
> L6: tldr; **No more floats.** Just weights in **[1, 0, -1]**.

## 星数曲线

```mermaid
xychart-beta
    title "kevbuh/bitnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d659737a38b3` · [字段定义](../../DATASET.md)*
