# marimo-team/codemirror-ai

⭐ 54 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/marimo-team/codemirror-ai) · [官网](https://marimo-team.github.io/codemirror-ai/) · 组织维护

**给编辑器开发者的 CodeMirror AI 编辑扩展库**

由 marimo 团队维护的 CodeMirror 扩展，为基于 CodeMirror 的编辑器提供 AI 辅助内联代码编辑能力：选中代码后通过键盘快捷键获取 AI 编辑建议，支持接受/拒绝建议界面与自定义快捷键；另提供 next edit prediction（下一处编辑预测）与 prompt history（提示历史）模块。以 npm 包形式分发，开发者引入 aiExtension 等扩展并在模板中构造提示词接入模型。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 辅助编辑：选中代码通过快捷键获取编辑建议，含接受/拒绝界面
- next edit prediction 内联补全模块
- prompt history 提示历史模块
- 自定义键盘快捷键

## 适用场景

- 在自研 CodeMirror 编辑器中加入 AI 内联编辑功能
- 为编辑器添加下一处编辑预测补全
- 复用提示历史管理用户与 AI 的交互记录

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A CodeMirror extension that adds AI-assisted inline code editing capabilities to your editor (like Continue.dev and 
> L24: import { aiExtension } from '@marimo-team/codemirror-ai';

## 星数曲线

```mermaid
xychart-beta
    title "marimo-team/codemirror-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-30 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ac45a137d52d` · [字段定义](../../DATASET.md)*
