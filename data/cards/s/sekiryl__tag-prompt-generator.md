# sekiryl/tag-prompt-generator

⭐ 22 · JavaScript · GPL-3.0 · 推送 2026-03-26 · [GitHub](https://github.com/sekiryl/tag-prompt-generator) · [官网](https://prompt-gen.sekiryl.is-a.dev) · 个人维护

**给艺术家与提示词工程师的交互式标签式 prompt 生成器**

基于 vanilla HTML/CSS/JavaScript 的网页应用，面向艺术家与 AI 提示词工程师：通过交互式标签系统（拖拽、快捷键排序）组合生成 prompt，支持自定义标签文件加载、输入自动补全、主题切换、prompt 保存与响应式移动端布局。运行方式为克隆仓库后用本地 HTTP 服务器提供服务（因浏览器 CORS 策略不能直接打开 index.html），标签排序依赖 Sortable.js，采用 GPL v3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 交互式标签系统：拖拽或键盘快捷键重排标签
- 加载自定义标签文件与输入自动补全建议
- prompt 保存管理与多主题切换
- 纯 vanilla HTML/CSS/JS，响应式移动端设计

## 适用场景

- 以 Danbooru 风格标签组合 AI 绘画提示词
- 导入自己的标签文件快速搭建 prompt 工作流
- 保存并复用常用标签组合

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A sleek, lightweight tag-based prompt generator.
> L6:  Built for artists and AI prompt engineers.

## 星数曲线

```mermaid
xychart-beta
    title "sekiryl/tag-prompt-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4ce60e04c5d1` · [字段定义](../../DATASET.md)*
