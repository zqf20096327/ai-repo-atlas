# louisecxqiu-glitch/html-doc-center

⭐ 10 · JavaScript · MIT · 推送 2026-07-30 · [GitHub](https://github.com/louisecxqiu-glitch/html-doc-center) · 个人维护 · 中文 README

**为 AI 生成的 HTML 提供浏览、编辑与版本历史的本地工作台**

基于 Python/aiohttp 的本地 Web 应用：自动扫描指定目录中的 HTML/MD 文件，生成可搜索的目录树，支持内联编辑、2 秒空闲自动快照、收藏排序、多扫描根配置与拖拽移动。v3.0 提供三模式编辑内核（GrapesJS 可视化/ProseMirror 富文本/CodeMirror 6 源码）、14 个可拖拽组件、属性面板与版本历史；选中文字可调用 AI 编辑，结果需人工接受。支持下载 macOS/Windows 可执行文件、源码双击启动或作为 Claude Code Plugin 通过 MCP 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三模式编辑：GrapesJS/ProseMirror/CodeMirror 6，快捷键 Alt+D/R/S 切换
- AI 文本编辑带 diff 预览与 Accept/Reject/Regenerate，仅发送选中文本
- 版本快照记录内容哈希、时间戳与原因标签（pre-ai/pre-restore/manual）
- 零 npm/webpack 构建步骤，仅依赖 aiohttp

## 适用场景

- 集中浏览和编辑 AI 编码工具批量生成的 HTML 报告与仪表盘
- 无需打开源码即可对生成的页面做可视化修改
- 保留每次保存与 AI 编辑前的版本快照以便回滚
- 将 Markdown 教程转换为可粘贴到微信公众号的 HTML

## 场景标签

 · 领域:开发工具/文档编辑

## 证据(README 行号)

> L5: Stop opening HTML files one by one. HTML Studio turns any folder into a browsable, editable, auto-saving document hu
> L99: 1. Select text in Design or RichText mode
> L148: HTML Studio works as a Claude Code Plugin with MCP support:

## 星数曲线

```mermaid
xychart-beta
    title "louisecxqiu-glitch/html-doc-center 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `01de664dd618` · [字段定义](../../DATASET.md)*
