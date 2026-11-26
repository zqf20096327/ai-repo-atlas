# ctrimm/weight-space-programming

⭐ 6 · Python · NOASSERTION · 推送 2026-11-07 · [GitHub](https://github.com/ctrimm/weight-space-programming) · 个人维护

**用 LLM 直接写出精确实现美国福利公式权重的实验仓库**

该仓库验证 weight-space programming 思路：让语言模型仅凭规则文本、不经训练，直接写出小型神经网络的全部权重，使其精确计算 SNAP、EITC、SSI、Medicaid 四类福利金额公式，再在数万输入点上与公式比对。方法采用预注册协议、权重 SHA-256 冻结、通用前向评分器，并以同架构 Adam 训练网络作对照。仓库提供图表复现脚本（numpy + matplotlib）。README 明确声明它不是可用的福利计算器，也不能用于资格判定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 组实验：LLM 逐权重写出网络，误差达浮点噪声级，与训练基线对照
- 预注册协议：权重 SHA-256 冻结、通用前向评分器、训练网络作对照
- 包含用 2 参数权重编辑修复过期费率的网络编辑实验
- 图表可用 python3 脚本从实验产物重新生成

## 适用场景

- 复现或检验 weight-space programming 在可精确验证域上的效果
- 研究 LLM 直接写权重与训练网络在断点处的误差差异
- 查阅福利公式作为神经网络可精确表示对象的实验记录

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: This repo tests the claim of *weight-space programming* in the domain
> L121: Every experiment follows the same pre-registered discipline:
> L178: Regenerate all four with `python3 docs/make_figures.py` (numpy +

## 星数曲线

```mermaid
xychart-beta
    title "ctrimm/weight-space-programming 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-13", "2026-11-26"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-08 5 → 2026-11-26 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `e2442d16777e` · [字段定义](../../DATASET.md)*
