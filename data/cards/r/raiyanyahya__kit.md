# raiyanyahya/kit

⭐ 38 · JavaScript · MIT · 推送 2026-08-04 · [GitHub](https://github.com/raiyanyahya/kit) · [官网](https://thekit.dev) · 个人维护

**集成编辑器/浏览器/终端/邮件的 AI 开发者桌面工作区**

基于 Electron 的一体式开发者工作区，将代码编辑器（CodeMirror 6）、Chromium 浏览器、终端、Git 可视化面板、IMAP/SMTP 邮件客户端、本地日历、白板与自主 Agent 整合在单窗口中，各工具共享上下文：终端 /ai 命令默认感知打开的文件、浏览页面、日历与书签。Agent 具备 5 个工具（读写文件、列目录、执行命令、全文搜索），写文件与执行命令前需用户授权，支持 .kitrules/AGENT.md 项目规则，兼容 OpenAI 与 Anthropic。另有 Stairs 可视化流水线（AI/Shell/HTTP/File 四类步骤）。提供 GitHub Release 安装包，也可从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自主 Agent 带 5 个工具，敏感操作（写文件/执行命令）逐次授权
- 终端 /ai 命令默认携带打开文件、浏览器页面、日历、书签上下文，可 --model 切换模型
- Stairs 可视化流水线：AI/Shell/HTTP/File 步骤可串联并传递输出
- 编辑器/浏览器/终端内置 AI 动作（摘要、查错、生成测试、页面提取）

## 适用场景

- 在单窗口完成编码、查文档、跑命令、管 Git 的日常开发
- 让自主 Agent 按自然语言任务建项目、修 bug、写测试
- 把多步骤重复工作编排成一键流水线

## 场景标签

`编码 Agent` `AI 助手` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Your entire dev environment. One window. AI woven through everything.**
> L95: An autonomous AI agent you give tasks to in plain English. Not a chat window and not autocomplete. An actual agent 
> L117: Works with OpenAI and Anthropic. Models update automatically when new versions of the app are released.

## 星数曲线

```mermaid
xychart-beta
    title "raiyanyahya/kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `698f06072580` · [字段定义](../../DATASET.md)*
