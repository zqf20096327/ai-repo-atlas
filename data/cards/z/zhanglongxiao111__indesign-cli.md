# zhanglongxiao111/indesign-cli

⭐ 60 · JavaScript · MIT · 推送 2026-09-25 · [GitHub](https://github.com/zhanglongxiao111/indesign-cli) · [官网](https://github.com/zhanglongxiao111/indesign-cli/releases/latest) · 个人维护 · 中文 README

**让 AI Agent 通过 CLI 直接操作 Adobe InDesign 的工具桥**

把 Adobe InDesign 的自动化能力包装成 Agent 友好的命令行工具：注册表固定包含 150 个 InDesign 工具（文档、页面、母版、文本、样式、导出、Book、模板槽位、JSX 脚本执行等），叠加 server/session/script.run/export.verify/tool.batch 等原生命令，支持项目级插件接入（如内置 HTML↔InDesign 转换域）。Agent 可通过 tool domains/search/schema 按需加载工具说明以节省 token，输出为结构化 JSON。仅支持 Windows，需本机安装 InDesign 桌面版（推荐 2024-2026），通过 COM 链路连接。提供离线 Setup 安装与源码开发两种方式，非给人类手动排版的工具，也不是独立排版引擎。

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

- 150 个 InDesign 工具的注册表，覆盖文档/文本/样式/导出/Book/模板槽位/JSX 执行
- tool domains/search/schema 分域按需加载，减少 Agent 上下文占用
- export verify 验证 PDF/IDML 等导出物真实生成
- 项目级插件机制，内置 HTML↔InDesign 转换域（成品安装）

## 适用场景

- 让 AI Agent 自动生成画册、汇报文档、品牌手册等排版产物
- HTML/JSON/模板到 InDesign 的转换项目
- Agent 工作流中执行 JSX 脚本并验证真实导出结果

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: 让 AI Agent 直接操作 Adobe InDesign 的命令行工具。
> L7: `indesign-cli` 把 InDesign 的自动化能力包装成 Agent 友好的 CLI：Agent 可以查询工具、执行 JSX 脚本、调用排版能力、验证导出文件，并按需配合项目级 Skill 使用。
> L26: 它不是一个给人类手动排版的 CLI，也不是一个新的排版引擎。它更像是 AI 项目和 InDesign 之间的稳定桥梁。

## 星数曲线

```mermaid
xychart-beta
    title "zhanglongxiao111/indesign-cli 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29", "2026-10-31"]
    y-axis "stars" 57 --> 61
    line [58, 59, 60, 60]
```

2026-10-18 58 → 2026-10-31 60（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `72a08a072bd1` · [字段定义](../../DATASET.md)*
