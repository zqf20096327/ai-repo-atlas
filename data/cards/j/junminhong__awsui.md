# junminhong/awsui

⭐ 124 · Python · MIT · 推送 2026-08-23 · [GitHub](https://github.com/junminhong/awsui) · [官网](https://junminhong.github.io/awsui/) · 个人维护 · 中文 README

**为 CLI 与 AI 编码代理提供经校验的 AWS 上下文启动器**

Python CLI 工具，解决 AWS profile 命名因机器而异的问题：将项目环境名（dev/staging/prod）映射到本地 AWS profile，启动前通过 STS GetCallerIdentity 校验账号与 .awsui.yaml 中预期的 12 位账号 ID 是否一致，一致才启动 Claude Code、Codex、Kiro、Terraform 或任意 CLI；不一致则停止。共享的账号/区域配置入库，机器相关的 profile 绑定保存在本地。README 声明它不是安全沙箱，子进程启动后仍可改写环境变量。需 Python 3.11–3.14 与 AWS CLI v2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 启动前通过 STS GetCallerIdentity 校验账号，不匹配则拒绝启动
- 项目环境名到本地 profile 的映射，绑定不上库
- 支持以 uv/pip 安装，提供 init/bind/context/doctor 等命令
- 子进程环境会移除凭据覆盖变量，自身不存储 AWS 凭据

## 适用场景

- 在多环境（dev/prod）项目中避免误用错误 AWS 账号运行 Terraform 或 AI 代理
- 团队共享各环境预期账号与区域，个人仅绑定本地 profile
- 以校验过的上下文打开交互式 shell 运行组合命令

## 场景标签

 · 领域:云基础设施/开发者工具

## 证据(README 行号)

> L14:  Choose an environment, verify the account, and launch Claude Code, Codex, Kiro, Terraform, or any CLI in the right
> L32: - Run AI agents, Terraform, AWS CLI, scripts, and shells in the same verified
> L38: > [!IMPORTANT]

## 星数曲线

```mermaid
xychart-beta
    title "junminhong/awsui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-24 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `15d93dfba4a9` · [字段定义](../../DATASET.md)*
