# MrHs6/ai-architec-rhino

⭐ 4 · C# · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/MrHs6/ai-architec-rhino) · [官网](https://ai-arch.ir) · 个人维护

**给 Rhino 建筑师的 AI 建模插件：对话生成本土几何**

运行于 Rhino 8/9 的 Windows 插件，输入 `archtec` 命令打开 Studio 面板，从自然语言请求生成概念几何、检查模型尺寸与几何健康度、对选中对象进行移动/缩放/拉伸等编辑。提供两条对话路线：在 Rhino 内用自有 API key 聊天（OpenAI/OpenRouter/Gemini/Anthropic/xAI 等，带预览与 Apply 步骤），或通过本地 MCP 桥接 Codex/Claude Desktop 由客户端直接授权执行本土工具。0.6.1-beta 新增跨面板持久 MCP 会话与可编辑 Grasshopper 定义生成。需自备 API key，不含 BIM、工程模拟或渲染。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- API 与本地 MCP 双路线：预览 Apply 或客户端授权执行本土工具
- 本土几何目录：NURBS 放样、Brep 布尔、扫掠、封闭流形网格等，生成件带楼层/角色元数据
- 可编辑 Grasshopper 定义：发现组件、建滑块与连线、显式烘焙几何
- 196 项自动化检查与 OpenRouter 真实工作流验收记录

## 适用场景

- 在 Rhino 中用自然语言快速生成建筑概念模型
- 连接 Codex/Claude Desktop 通过 MCP 直接驱动建模工具
- 对既有模型做只读的尺寸、几何健康与图层检查
- 生成并迭代可编辑的 Grasshopper 参数化定义

## 场景标签

`代码生成` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L21: Open **`archtec`** inside Rhino to generate concept geometry, inspect your model or refine selected objects. Connec
> L67: The native catalog includes capped NURBS lofts, Brep booleans, sweeps, revolution, pipes, offsets, closed manifold 

## 星数曲线

```mermaid
xychart-beta
    title "MrHs6/ai-architec-rhino 星数(近 3 点)"
    x-axis ["2026-11-18", "2026-11-21", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-18 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `85d107bf32f2` · [字段定义](../../DATASET.md)*
