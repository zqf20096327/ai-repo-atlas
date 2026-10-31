# Kuberwastaken/picogpt

⭐ 134 · HTML · 推送 2026-02-17 · [GitHub](https://github.com/Kuberwastaken/picogpt) · [官网](https://kuber.studio/picogpt/) · 个人维护

**可塞进二维码的极简 GPT：纯 JS 训练与推理实现**

受 Andrej Karpathy 的 MicroGPT 启发的最小化 GPT 实现：39 行纯 JavaScript 包含自研 Autograd 引擎、多头注意力、GeLU 近似的 MLP、AdamW 优化器与余弦学习率调度，完成训练与推理循环，无任何依赖。整个 HTML 页面经 gzip+base64 压缩后嵌入 version-40-L 二维码（2953 字节），扫码即可在浏览器中训练模型；另有 64 行的旧版 Python 实现保存在 legacy 目录。模型为 1 层、4 头、4,064 参数的小型架构。

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

- 39 行纯 JS 实现含 Autograd、MHA、AdamW 的训练与推理
- 整个实现压缩后嵌入 version-40-L 二维码（2953 字节）
- 扫码后浏览器通过 DecompressionStream 解压并原地训练
- 附 64 行旧版 Python 实现（legacy/ 目录）

## 适用场景

- 学习 GPT 最小可运行实现的教学演示
- 扫码在浏览器中直接体验模型训练
- 研究代码极度压缩与二维码载荷分发方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L25: It works in **JUST 39 LINES** of pure JavaScript!
> L33: - Training & Inference loops

## 星数曲线

```mermaid
xychart-beta
    title "Kuberwastaken/picogpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-31 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a5a179c48174` · [字段定义](../../DATASET.md)*
