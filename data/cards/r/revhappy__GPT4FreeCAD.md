# revhappy/GPT4FreeCAD

⭐ 68 · Python · MIT · 推送 2026-08-08 · [GitHub](https://github.com/revhappy/GPT4FreeCAD) · 个人维护

**FreeCAD 工作台：用自然语言生成可编辑的参数化 CAD 几何**

FreeCAD 插件，把英文描述经 LLM（Gemini/OpenAI/Claude/Grok/OpenRouter 或本地 GGUF/Ollama/LM Studio 模型）转换为经 schema 校验的结构化 JSON CAD 程序（IR），由确定性解释器构建成原生 FreeCAD 参数化特征树，生成后可手工编辑。提供工程模式特征时间线、3D 打印模式、STL/STEP 导出、构建后几何检查与多轮自动修复、六个内置参数化模板。本地模型路径通过 llama.cpp 采样器内 GBNF 语法约束输出，无需 API key；v2 仅用标准库，无第三方依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言→校验后的结构化 JSON IR→原生 FreeCAD 参数化特征树
- 构建后几何检查（封闭/非零体积）+ 多轮自动修复（默认 3 轮）
- 本地 GGUF 模型路径经 GBNF 语法在 llama.cpp 采样器内强制约束，无需 API key
- 支持 Gemini/OpenAI/Claude/Grok/OpenRouter 及 Ollama/LM Studio 服务器，模型列表实时拉取

## 适用场景

- 用一句话描述零件，快速生成可继续手工编辑的 FreeCAD 参数化模型
- 3D 打印前按打印机成型体积约束零件并导出 STL
- 离线环境用本地模型生成 CAD 几何，数据不离开本机
- 从模板库（法兰、L 支架、齿轮坯等）起步再让 AI 修改参数

## 场景标签

 · 领域:CAD/工程工具

## 证据(README 行号)

> L3: Generate **parametric** FreeCAD geometry from plain English — powered by your choice of
> L152: |Output|raw `exec()` of model text|**validated structured IR** → parametric objects, *or* opt-in Python mode|
> L162: Your description ──▶ LLM (Gemini/OpenAI/Claude/local) ──▶ JSON program

## 星数曲线

```mermaid
xychart-beta
    title "revhappy/GPT4FreeCAD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 66 --> 69
    line [67, 68, 68]
```

2026-10-18 67 → 2026-10-24 68（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d74bd8526465` · [字段定义](../../DATASET.md)*
