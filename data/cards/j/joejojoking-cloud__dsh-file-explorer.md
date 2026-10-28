# joejojoking-cloud/dsh-file-explorer

⭐ 21 · TypeScript · 推送 2026-08-31 · [GitHub](https://github.com/joejojoking-cloud/dsh-file-explorer) · 个人维护 · 中文 README

**DeepSeek Harness 的全局文件资源管理器插件**

面向 DeepSeek Harness 的右侧面板插件：在会话标题栏提供文件树入口，支持可调宽度面板（260–900px）、浏览器式多标签文件预览、Markdown 渲染与按扩展名语法高亮、面板内编辑并写回磁盘、一键在 VS Code 或系统文件管理器中打开，以及跳过 .git/node_modules 的工作区递归搜索（最多 300 条）。超过 1 MB 的文件不支持预览。通过 dsh plugin 命令安装，重启 harness 后对所有会话生效；源码分 host 与 web client 两半部，构建后由内容哈希自动换新。

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

- 右侧可调宽度文件树 + 独立收起的预览面板
- 浏览器式多标签预览：Markdown 渲染与按扩展名语法高亮，面板内编辑写回磁盘
- 一键 VS Code / 系统文件管理器打开，双击聊天区按项目过滤标签
- 递归工作区搜索，跳过 .git/node_modules，上限 300 条

## 适用场景

- 在 DeepSeek Harness 会话中直接浏览和编辑项目文件
- 预览 Markdown 与代码文件而不离开对话界面
- 从插件快速跳转到 VS Code 或系统文件管理器继续操作

## 场景标签

 · 领域:AI Agent 工具链/文件管理

## 证据(README 行号)

> L3: > **File Explorer for DeepSeek Harness** — right-side resizable file tree with Markdown rendering, syntax highlighti
> L5: DeepSeek Harness 的全局文件资源管理器插件：在任何会话的标题栏右侧提供文件夹切换按钮，点击后在页面**右侧**打开可调宽度的文件树面板。
> L29: - `src/client/index.ts` — web client 半部（`tsc` → `lib/client/index.js` → `tsdown` → `lib/client.js`）：注册 `shell.overl

## 星数曲线

```mermaid
xychart-beta
    title "joejojoking-cloud/dsh-file-explorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4efd46fa6b22` · [字段定义](../../DATASET.md)*
