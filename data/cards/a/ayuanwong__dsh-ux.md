# ayuanwong/dsh-ux

⭐ 14 · TypeScript · BSD-3-Clause · 推送 2026-08-16 · [GitHub](https://github.com/ayuanwong/dsh-ux) · 个人维护 · 中文 README

**DeepSeek Harness 的社区 Web UX 版：长任务进度清晰、完成后自动折叠**

DeepSeek Harness 的非官方社区源码分支，不改变 Agent Loop、模型路由、工具与沙箱，重点改进网页界面：任务运行时把思考与工具调用收进稳定过程区并显示当前步骤与耗时，完成后自动折叠、失败保持展开；长日志独立滚动、会话搜索排序、生成文件入口识别、模型配置集中到设置页。可选展示辅助用一次小模型请求整理阶段名称，不修改原始回答。仅提供源码运行（Node.js 22+/pnpm 11），不发布 npm 包，无内建 Codex OAuth 登录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行中过程收进稳定区域，展示当前步骤与运行时长
- 任务完成自动折叠过程、失败或中断保持展开
- 识别答案中列出的文件路径并显示为可打开产物入口
- 可选展示辅助整理阶段名称，不修改原始回答与会话历史

## 适用场景

- 在网页里跟进 DeepSeek Harness 长任务的进度
- 任务完成后快速定位最终答案，需要时展开细节
- 搜索历史会话与查找任务生成的文件

## 场景标签

 · 领域:AI Agent 工具/开发者工具

## 证据(README 行号)

> L7: DeepSeek Harness UX 是一个非官方社区源码版本。它没有重写 Agent 的工作方式，而是重点改进网页里的任务过程、长回答、会话查找和文件入口。
> L55: - Agent Loop、模型路由、工具、权限、沙箱和 Session Log 仍沿用 DeepSeek Harness 的执行方式。

## 星数曲线

```mermaid
xychart-beta
    title "ayuanwong/dsh-ux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5d2ce891132a` · [字段定义](../../DATASET.md)*
