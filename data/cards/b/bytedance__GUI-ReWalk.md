# bytedance/GUI-ReWalk

⭐ 42 · Python · Apache-2.0 · 推送 2026-05-01 · [GitHub](https://github.com/bytedance/GUI-ReWalk) · [官网](https://gui-rewalk.github.io/) · 组织维护 · 中文 README

**为 GUI Agent 合成大规模操作轨迹数据的多阶段框架**

论文官方代码，用于生成 GUI agent 训练所需的轨迹数据：先通过随机探索模拟人类试错行为，再转入由推断目标驱动的推理引导阶段，支持跨应用的多步长任务生成、回溯式 LLM 标注与错误恢复机制。运行依赖 VMware 虚拟机与 OSWorld 环境，配合 OmniParser，通过 LLM API（如豆包/ARK）执行生成，bash 脚本启动，参数控制轨迹长度、随机动作数与质量阈值等。作者还基于该数据集训练了 GUI-ReWalk-7B 并在多个基准上评测。

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

- 随机探索与推理引导结合的多阶段轨迹生成
- 支持跨应用长程任务与错误恢复机制
- 基于该数据集训练 GUI-ReWalk-7B 并在 Screenspot-Pro/OSWorld-G 等基准评测
- 数据覆盖移动端与桌面端多平台

## 适用场景

- 为 GUI agent 训练合成高质量、多样化的操作轨迹数据
- 研究生成轨迹的熵、意图真实性与 token 成本
- 构建跨应用的长程任务工作流数据

## 场景标签

 · 领域:GUI Agent/数据生成

## 证据(README 行号)

> L5: Graphical User Interface (GUI) Agents, powered by large language and vision-language models, hold promise for enabli
> L73: bash run_rewalk.sh

## 星数曲线

```mermaid
xychart-beta
    title "bytedance/GUI-ReWalk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c5dfdc28cb8b` · [字段定义](../../DATASET.md)*
