# AwesomeHou/dsh-plugin-marketplace

⭐ 33 · JavaScript · MIT · 推送 2026-09-12 · [GitHub](https://github.com/AwesomeHou/dsh-plugin-marketplace) · 个人维护 · 中文 README

**DeepSeek Harness 插件：把 GitHub dsh-plugin 话题变成插件市场**

作为 DeepSeek Harness 的永久插件运行：通过 GitHub Search API 实时同步 `dsh-plugin` 话题下的仓库，在“设置→插件”中提供可搜索、分页的插件市场与已安装标签页，支持一键安装（npm 包优先、monorepo 克隆构建）、更新、停用与卸载，安装任务带进度条与停滞看门狗。同时注册 market_search / market_install 等 agent 工具，让 agent 自行搜索并安装插件；直装失败时可“让 agent 安装”在专属工作区新开会话处理。手动安装用 `dsh plugin add` 命令并需重启 harness。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时同步 GitHub dsh-plugin 话题为可搜索分页的插件市场
- 提供 market_search/market_install/market_installed/market_update 四个 agent 工具
- 确定性异步安装：npm 包优先、pnpm 失败分类、停滞看门狗与结果校验
- 支持插件的更新/停用/启用/卸载，写 profile 操作 FIFO 串行落盘

## 适用场景

- 在 harness 设置页浏览并一键安装 dsh-plugin 话题下的插件
- 让 agent 通过工具自行搜索并安装所需插件
- 管理已安装第三方插件的版本更新与停用/卸载

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: 一个 DeepSeek Harness 的**永久插件**，把 GitHub
> L19: - **Agent 工具**（Host 侧通过 `ctx.tools.register` 注册）：
> L44: dsh plugin --profile web add https://github.com/AwesomeHou/dsh-plugin-marketplace

## 星数曲线

```mermaid
xychart-beta
    title "AwesomeHou/dsh-plugin-marketplace 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-30 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ba53dcf1a1c5` · [字段定义](../../DATASET.md)*
