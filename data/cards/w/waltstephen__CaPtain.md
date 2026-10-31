# waltstephen/CaPtain

⭐ 27 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/waltstephen/CaPtain) · 组织维护

**把小视觉语言模型后训练成代码即策略机器人智能体的开源全流程管线**

面向具身智能/机器人学习研究者的代码即策略（CaP）后训练管线：将 Qwen3.5-4B 经 SFT（合成轨迹数据）与 RL（读取仿真器物理状态的模拟器 critic 提供信用）训练为 CaPtain-4B，智能体在带 22 项底层能力（感知、几何测量、IK 级运动）的沙箱 Python 会话 CaPtain-Harness 中编写代码控制机器人并自行判定任务完成。开放 SFT 数据、模型权重、训练代码与 RL 基础设施。评测需 Linux x86_64 与 NVIDIA GPU，SFT/RL 训练需 16×H100 级硬件，支持 LIBERO 系列、RoboTwin 2.0、RoboDojo、SimplerEnv 等基准后端及真实机器人接口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CaPtain-Harness：22 项底层能力、每次调用返回文本回执的持久沙箱 Python 会话，同一 API 覆盖多基准与真实机器人
- RL 采用模拟器 critic：读取仿真器物理状态将预测成功率变化转为信用，策略本身不可见该状态
- 开放 SFT 数据、模型权重、训练代码与 RL 基础设施（流式 rollout 服务器、run supervisor）
- 任意 OpenAI 兼容端点均可作为策略后端（POLICY_URL），可运行前沿模型或自有 checkpoint

## 适用场景

- 在 LIBERO 系列基准上评测 CaPtain-4B 或自有模型的代码即策略能力
- 复现或修改 SFT→RL 后训练流程训练自己的 CaP 智能体
- 通过实现 adapters 后端接入新机器人或新基准
- 做零样本迁移评测（RoboTwin 2.0 / SimplerEnv / RoboDojo 等）

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L15: CaPtain post-trains a small open vision-language model into a **code-as-policy (CaP) robot agent**: the agent contr
> L27: - **CaPtain-4B** — Qwen3.5-4B after SFT and RL. At test time it uses neither a frontier model nor a benchmark-train


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `af745cc2d23e` · [字段定义](../../DATASET.md)*
