# cookiy-ai/cookiy-cli

⭐ 14 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/cookiy-ai/cookiy-cli) · [官网](https://cookiy.ai) · 组织维护

**Cookiy AI 的命令行客户端：终端执行用户研究与量化调研**

Cookiy AI 服务的 CLI 客户端，通过终端运行用户研究、AI 访谈、合成用户、量化问卷与参与者招募等操作。以 npm 全局包形式安装（需 Node.js 18+），命令为 cookiy / cookiy-cli。面向 REST V1 API 封装：成功输出 data 到 stdout，错误以 JSON 格式输出到 stderr 并非零退出；支持 --base-revision 乐观并发、study/report 轮询等待、CSV 原始响应导出，并保留部分已弃用参数兼容旧用法。需配合 Cookiy 服务端使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- V1 REST 请求/响应约定封装：JSON 错误码与退出状态规范
- study report wait 轮询机制（15 秒间隔、超时预算控制）
- guide 更新支持嵌套与点号键两种 JSON 写法及乐观并发
- 支持 CI 环境通过环境变量禁用后台更新检查

## 适用场景

- 在终端创建和管理用户研究 study 与访谈指南
- 导出量化问卷原始响应为 CSV
- 在 CI/自动化脚本中集成 Cookiy 用户研究流程

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Command-line client for Cookiy AI — run user research, quant surveys, and recruit participants from your terminal.
> L28: - Successful V1 responses print `data` to stdout. Standard API errors print the server's `error` to stderr and exit

## 星数曲线

```mermaid
xychart-beta
    title "cookiy-ai/cookiy-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5dea3fb1ba30` · [字段定义](../../DATASET.md)*
