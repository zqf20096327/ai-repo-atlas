# Concode0/clifra

⭐ 61 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/Concode0/clifra) · [官网](https://concode0.github.io/clifra/) · 个人维护

**PyTorch 的可微 Clifford 代数计算层库**

面向 PyTorch 的 Clifford（几何）代数计算层：以签名（signature）定义基向量乘积，以 grade layout 选择系数通道，支持紧凑或规范存储的张量约定；运算可先规划一次再复用，系数值与前置张量维度保持为普通 PyTorch 输入，从而可微。面向做几何代数深度学习的开发者，通过 uv/pip 安装，附教程、指南、研究与模型基准文档，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可微的 Clifford 代数运算，系数张量为普通 PyTorch 输入
- 签名 + 布局 + 存储约定的声明式描述
- 运算可规划一次并复用

## 适用场景

- 在 PyTorch 模型中引入几何代数运算
- 构建几何代数深度学习研究原型
- 查阅模型基准对比 Clifford 运算实现

## 场景标签

 · 领域:深度学习/几何代数计算库

## 证据(README 行号)

> L7: clifra is a differentiable Clifford algebra computation layer for PyTorch.
> L12: uv add clifra

## 星数曲线

```mermaid
xychart-beta
    title "Concode0/clifra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-29 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ccd08986aa8e` · [字段定义](../../DATASET.md)*
