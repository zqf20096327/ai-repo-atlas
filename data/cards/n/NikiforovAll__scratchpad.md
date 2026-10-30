# NikiforovAll/scratchpad

⭐ 16 · TypeScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/NikiforovAll/scratchpad) · [官网](http://nikiforovall.blog/scratchpad/) · 个人维护

**为 AI agent 组织临时知识到 scratchpad 文件夹的 CLI，带只读查看器**

CLI 工具，将 agent 会话产生的笔记、代码片段、中间产物组织到 scratchpad——一个含 scratchpad.json 清单的文件夹，无中心存储，CLI 仅初始化、注册文件、打印用法，不创作或移动内容。附带只读可视化查看器（原生窗口或浏览器回退），支持 Markdown 渲染、代码高亮、KaTeX 数学、Mermaid 图，可添加行内评论供 agent 通过 scratch comments 读回形成反馈循环。面向使用编程 agent 的开发者，运行于 Bun 运行时，可构建独立二进制；另提供 Claude Code 插件与 pi agent 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- scratchpad = 文件夹 + scratchpad.json 清单，无中心存储、无锁定
- 只读查看器支持 Markdown/代码高亮/KaTeX/Mermaid/行内评论
- agent 可通过 scratch comments --json 读回人类评论形成反馈循环
- 可构建无需 Bun 的独立二进制

## 适用场景

- 给 agent 会话的临时笔记和中间产物一个持久可浏览的存放处
- 人工查看 agent 收集的知识并留评论让 agent 接续工作
- 在源码树之外管理工作记忆，删除文件夹即彻底移除

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: CLI-first tool to organize **agent knowledge** into *scratchpads* — a folder of files plus a `scratchpad.json` manif
> L12: A scratchpad is **just a folder containing `scratchpad.json`**; the folder path is its identity. There is **no cent

## 星数曲线

```mermaid
xychart-beta
    title "NikiforovAll/scratchpad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d0d740bc9f56` · [字段定义](../../DATASET.md)*
