# lucidrains/discrete-continuous-embed-readout

⭐ 20 · Python · MIT · 推送 2026-07-05 · [GitHub](https://github.com/lucidrains/discrete-continuous-embed-readout) · 个人维护

**离散/连续分布的嵌入与读出 PyTorch 组件库**

由 lucidrains 维护的 PyTorch 组件库，提供 EmbedAndReadout 模块，将类别分布与高斯连续分布统一为可微的嵌入与读出接口，覆盖语言建模、离散动作空间、连续控制/回归、混合动作空间与多离散动作空间等场景，另支持运行时动态定义输入选择器，供跨模态共享嵌入的架构使用。以 pip 包形式安装，面向构建自回归模型或机器人动作策略的研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- EmbedAndReadout 统一处理类别与高斯连续分布
- 支持离散、连续、混合、多离散四类动作/输出空间
- 运行时动态选择器，可跨模态共享嵌入

## 适用场景

- 为自回归语言模型构建可微的输出读出层
- 机器人连续/混合动作空间的策略输出建模
- 回归任务的高斯分布输出读出

## 场景标签

 · 领域:深度学习/机器人

## 证据(README 行号)

> L3: Embedding and readout for simple categorical and gaussian distributions, from the language model to sophisticated ro
> L15: For standard autoregressive language modeling or discrete action spaces.

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/discrete-continuous-embed-readout 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bf18ef17b6d6` · [字段定义](../../DATASET.md)*
