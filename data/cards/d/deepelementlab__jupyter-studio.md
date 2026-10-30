# deepelementlab/jupyter-studio

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-05-18 · [GitHub](https://github.com/deepelementlab/jupyter-studio) · 组织维护

**给数据科学研究者的带 AI agent 的 JupyterLab 扩展**

以 JupyterLab 扩展与跨平台桌面应用两种形式提供的 AI 编码环境：在 notebook 内提供 Cmd+K 内联编辑、多步 agent（含 read_cell/edit_cell/run_cell 等单元格级工具）、@cell/@file 上下文聊天、Ghost Text 补全与一键修复 traceback。模型通过 .clawcode.json 配置接入 Anthropic、OpenAI、Google、Azure、Ollama、vLLM 等 OpenAI 兼容端点，默认无遥测。仓库含 clawcode agent 运行时、jupyter_server 扩展与 JupyterLab Desktop 分支三个包，本地开发需 pip + jlpm 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Cmd+K 内联编辑与 Ghost Text 补全，工作在任意单元格内
- 多步 agent 具备 read/edit/insert/run cell 单元格级工具
- 一键诊断并修补出错单元格的 traceback 修复
- BYO 模型：支持 Anthropic/OpenAI/Google/Azure/Ollama/vLLM 及 OpenAI 兼容端点

## 适用场景

- 在 notebook 内直接让 agent 跨单元格重构与修错
- 把 ChatGPT 来回粘贴的工作流替换为同 kernel 的对话式编辑
- 用本地 Ollama/vLLM 模型做隐私优先的代码补全

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L24: **Jupyter Studio brings the Cursor-class AI editing experience *into JupyterLab itself*** — same notebook, same ker
> L37: - 🖥 **Desktop or browser** — ships as a JupyterLab extension *and* a native cross-platform desktop app.
> L91: |Windows 10/11|macOS 12+|Linux|

## 星数曲线

```mermaid
xychart-beta
    title "deepelementlab/jupyter-studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `13f504cdaa4e` · [字段定义](../../DATASET.md)*
