# OpenRaiser/NeurCo

⭐ 3 · MIT · 推送 2026-11-22 · [GitHub](https://github.com/OpenRaiser/NeurCo) · [官网](https://openraiser.github.io/NeurCo/) · 组织维护

**把视频生成模型当可编程渲染器：编译请求为可执行计划**

NeurCo 是一个视频生成编译框架：离线对冻结的视频模型做探测打分，产出能力手册（各控制在各难度、各输入模式下的成功率与 ok/weak/bad/unknown 状态）；在线将请求解析为对象、约束、事件、相机的模型无关中间表示，对照能力手册保留已支持的要求，弱项改写为文本、补充参考图/首帧/代理视频/镜头拼接等外部操作。附带 VComBench 基准（380 个组合任务、34 个控制、1,617 条评分要求），覆盖 T2V/I2V/R2V，并在 H3、Wan、Seedance 2.5 上给出 VBench-2.0 与 Sci-VBench 结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 离线能力探测生成 ok/weak/bad/unknown 状态的能力手册
- 请求编译为模型无关 IR（对象/约束/事件/相机）再执行
- 弱项要求自动改写文本或路由到外部操作符
- VComBench：380 任务、34 控制、1,617 条评分要求

## 适用场景

- 为视频生成模型构建可控组合式生成的执行计划
- 评估视频模型在不同控制与难度下的能力边界
- 组合任务中部分要求失败时改写或路由到外部操作

## 场景标签

`视频生成` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: NeurCo probes a frozen video model and turns what that model can reliably do into a capability manual. A request is
> L35: VComBench has 380 compositional tasks across T2V, I2V, and R2V, with 1,617 scored requirements over 34 controls. Th


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `dfa0489b776e` · [字段定义](../../DATASET.md)*
