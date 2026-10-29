# ursazoo/lanhu-to-code

⭐ 23 · Shell · 推送 2026-05-12 · [GitHub](https://github.com/ursazoo/lanhu-to-code) · 个人维护 · 中文 README

**把蓝湖设计稿链接转成前端代码的 Claude Code Skills 工具集**

面向 Claude Code 的一组前端工作流 skills：用户粘贴蓝湖页面 URL，Claude Code 通过蓝湖 MCP 读取设计稿结构、样式与切图，检查项目工程规范文档，优先复用已有组件（docs/components.md），把颜色、间距等原始值映射为项目 design token，生成 Vue/React 或项目描述技术栈的代码；不确定的 API、枚举与业务逻辑标记 TODO 而非编造，生成后可选择 code review。含 4 个 skill（design-to-code/code-gen/code-format/component-doc-gen），通过 git clone 与 install.sh 安装，依赖独立部署的蓝湖 MCP 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个 skill 覆盖设计读取、代码生成、格式转换与组件文档生成
- 通过 Lanhu MCP 读取设计稿，code-gen 在隔离子代理上下文运行
- 优先复用项目已有组件并将设计值映射为 design token
- 不确定内容标记 TODO，不猜测后端契约与枚举值

## 适用场景

- 前端团队把蓝湖设计稿转为符合项目规范的 Vue/React 代码
- 生成时复用项目已有组件而非重复造轮子
- 生成后对 AI 产出代码做风格漂移与 TODO 检查的 code review

## 场景标签

`代码生成` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L17: `lanhu-to-code` packages that workflow into Claude Code skills. Paste a Lanhu page URL, and Claude Code follows a s
> L48: |`design-to-code`|`/design-to-code`|Main workflow. Runs prerequisite checks, design extraction, code generation, an
> L119: claude

## 星数曲线

```mermaid
xychart-beta
    title "ursazoo/lanhu-to-code 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-29 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3be787e20b83` · [字段定义](../../DATASET.md)*
