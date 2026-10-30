# neuronaline/local-ai-cad-agent

⭐ 16 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/neuronaline/local-ai-cad-agent) · 个人维护

**本地/云端对话式生成参数化 3D CAD 模型的 Web 应用**

通过自然语言与参考图片生成和修改参数化 OpenSCAD 模型的 Web 应用，面向 3D 打印用户与 CAD 开发者。Agent 以 7 个结构化工具迭代读写 model.scad，在 Bubblewrap 隔离沙箱（断网、只读挂载、seccomp 过滤）内编译并验证流形拓扑、体积与边界，渲染 8 视角图供视觉自检。可完全离线经 Ollama 运行，或接入 OpenRouter/OpenAI/Gemini/Vertex AI；支持 Three.js 实时预览、多格式导出（3MF/STL/OBJ 等）与打印参数建议。限 Linux/WSL2，服务绑定 127.0.0.1 且无内置鉴权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成与编辑参数化 OpenSCAD 模型，支持参考图片
- Bubblewrap 沙箱隔离执行 OpenSCAD 与数学脚本（断网+seccomp）
- 流形拓扑/体积/边界确定性验证与 8 视角视觉自检
- Ollama 完全离线运行，或接入 OpenRouter/OpenAI/Gemini/Vertex AI

## 适用场景

- 对话式设计可直接 3D 打印的参数化零件
- 离线环境下用本地模型迭代 CAD 设计
- 导出 3MF/STL 等格式进入切片与打印流程

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: A local-first web application for **creating and refining parametric 3D CAD models through natural language**. Built
> L16: - **Chat-Driven Parametric CAD:** Authors and edits clean, parametric OpenSCAD (`model.scad`) from text prompts and

## 星数曲线

```mermaid
xychart-beta
    title "neuronaline/local-ai-cad-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b120e84ce716` · [字段定义](../../DATASET.md)*
