# mizuirorivi/slidev-overflow-checker

⭐ 23 · TypeScript · MIT · 推送 2026-01-17 · [GitHub](https://github.com/mizuirorivi/slidev-overflow-checker) · 个人维护 · 中文 README

**为 AI agent 检测 Slidev 幻灯片视觉溢出的 CLI 工具**

基于 Playwright 在真实浏览器中渲染 Slidev 幻灯片、逐页检测溢出的命令行工具，输出像素级溢出度量与源码行号映射，供 AI agent（如 Claude Code、Cursor）解析并自动修复布局问题。检测类型覆盖文本溢出、元素越界与非预期滚动条，支持 console/json/html 输出、阈值设置、--fail-on-issues 退出码用于 CI。需 Node.js 18+ 与 Slidev 0.40+，要求 Slidev 开发服务器在运行中。

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

- Playwright 真实浏览器渲染并按像素度量溢出，报告对应 Markdown 源码行
- 结构化输出（console/json/html）供 AI agent 解析执行
- 支持指定页范围、溢出阈值、CI 失败退出码与配置文件
- 提供 Claude Code 命令模板（/fix-slidev-overflow）实现自动检测-修复-验证循环

## 适用场景

- AI 生成 Slidev 演示文稿后自动检测并修复布局溢出
- CI 流水线中阻断存在溢出问题的幻灯片构建
- 开发者逐页排查文本越界、元素越界与滚动条问题

## 场景标签

 · 领域:开发工具/演示文稿质量检测

## 证据(README 行号)

> L3: **Detect visual overflow in Slidev presentations through real browser rendering.**
> L5: Designed for **AI agents** to automatically find and fix layout issues that cannot be detected from Markdown alone.
> L24: - **AI-Friendly Output** - Structured output that AI agents can parse and act on

## 星数曲线

```mermaid
xychart-beta
    title "mizuirorivi/slidev-overflow-checker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c81f919d2aab` · [字段定义](../../DATASET.md)*
