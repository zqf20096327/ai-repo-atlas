# tensorviz-org/tensorviz

⭐ 8 · TypeScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/tensorviz-org/tensorviz) · [官网](https://tensorviz.dev) · 组织维护

**给 PyTorch/JAX 开发者把模型可视化为交互式计算图**

以 VS Code 扩展与编码代理插件形式提供的模型可视化调试工具：将 PyTorch 与 JAX/Flax 模型渲染为交互式图，检查张量形状、跳转到对应 Python 源码，并可在编辑器或编码代理中审查模型变更。捕获机制实际执行一次模型前向调用以记录形状，也提供不运行模型的源码预览模式；配置保存在 tensorviz.toml。分发覆盖 VS Code/Cursor/VSCodium 扩展及 Codex/Claude Code 插件目录，MIT 许可但依赖的 tldraw 渲染组件不在该许可覆盖内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 交互式计算图展示张量形状并跳转到 Python 源码声明
- 编码代理插件支持通过对话打开图与检查模型
- 源码预览模式不运行模型，捕获模式执行一次前向调用
- 支持 PyTorch 与 JAX/Flax 两类框架

## 适用场景

- 调试模型时检查每层的输入输出张量形状
- 在编码代理对话中让 AI 打开并讲解模型结构
- 代码审查时查看模型变更对应的图差异

## 场景标签

 · 领域:开发工具/深度学习调试

## 证据(README 行号)

> L8:  Explore your PyTorch or JAX/Flax model as an interactive graph. Follow tensor shapes, find the matching Python, and
> L100: |Agent cannot see tools|Start a new chat. For the extension, see Connect MCP|
> L130: |`packages/contracts`, `packages/graph-host`|Shared protocol and MCP host|

## 星数曲线

```mermaid
xychart-beta
    title "tensorviz-org/tensorviz 星数(近 3 点)"
    x-axis ["2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 2 --> 9
    line [3, 7, 8]
```

2026-11-20 3 → 2026-11-22 8（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e97db33516f4` · [字段定义](../../DATASET.md)*
