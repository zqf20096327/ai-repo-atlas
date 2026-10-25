# leehanchung/SMILE-factory

⭐ 106 · Python · Apache-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/leehanchung/SMILE-factory) · 个人维护

**合成数据驱动的深度研究训练工厂，含 Discord 编排 Claude Code 的机器人**

定位为合成数据游乐场/工厂：生成深度研究任务、经 agent 执行、用 BenchFlow 评测轨迹并回灌 RL/LoRA 训练，共八个分区（任务生成、评测、agent 循环、工具服务、RL/SFT 训练、编排与基础设施）。README 详述其中 Delulu 编排器：Discord 机器人将用户请求派发到 Modal 临时沙箱中运行 Claude Code，会话状态持久化在 Modal Volume 上支持 --continue 续聊，OAuth 凭据不经宿主机落盘。需要 Discord/Modal/Claude 订阅账号，机器人进程本身约 50MB 内存，可用 Docker 部署到低配 VPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 合成任务生成→agent 执行→评测→RL/LoRA 训练的闭环流水线
- Delulu：Discord @提及触发 Modal 沙箱内运行 Claude Code，线程内自动续会话
- Claude OAuth 凭据仅存于 Modal Secret 与 Volume，宿主机不落盘
- 支持 /commit 将工作区成果推送回 GitHub

## 适用场景

- 在 Discord 里通过对话让 Claude Code 完成任务并延续上下文
- 批量生成深度研究合成任务并评测 agent 轨迹
- 用 RL 或 LoRA SFT 配方将评测信号回灌训练模型

## 场景标签

`编码 Agent` `模型评测` `微调` · 领域:编码与开发

## 证据(README 行号)

> L27: The deep-research loop is the spine: `data/datagen` → `eval` → `training/rl_deepresearch`,
> L35: Discord bot that dispatches Claude Code tasks to ephemeral Modal Sandboxes.
> L41: 3. Bot dispatches the task to a Modal Sandbox (ephemeral container with Claude Code installed)

## 星数曲线

```mermaid
xychart-beta
    title "leehanchung/SMILE-factory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-25 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `6ed5b7922116` · [字段定义](../../DATASET.md)*
