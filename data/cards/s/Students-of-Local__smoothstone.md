# Students-of-Local/smoothstone

⭐ 83 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Students-of-Local/smoothstone) · 个人维护

**让小模型本地生成可打印 3D 零件的技能与 CLI**

smoothstone 提供一个名为 stone 的命令行工具与 agent 技能：模型不直接写几何代码，而是从 17 个经过测试的 recipe 中选择并填入尺寸，由工具调用 OpenSCAD 构建并对 STL 做切片器视角的打印检查（水密、壁厚、悬垂角等）。支持从文字或图片生成，图片路径提供轮廓描摹、高度图与参照物测距；人偶流程在 Apple silicon 上串联三个本地模型完成描述、渲染与网格化。构建状态通过 NEXT 行落盘，模型上下文被压缩后可经 stone status 继续。安装需 uv、OpenSCAD（Manifold 后端）与 potrace。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个免支撑 recipe，默认值与示例在 CI 中构建检查
- 构建检查覆盖水密性、壁厚、45 度悬垂与承诺尺寸
- 图片输入：轮廓描摹、lithophane 高度图、参照物实测毫米尺寸
- 上下文压缩后凭 NEXT 行与 stone status 恢复任务

## 适用场景

- 让本地小模型从一句描述生成可直接打印的零件
- 从照片生成钥匙扣、浮雕、lithophane 等实物
- 在无 GPU 的 CPU 环境下运行 3D 打印生成流程
- 为 llama.cpp/llama-server 上的模型提供 stone 工具与技能卡

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: I wanted a small model running on my own computer to make 3D printable parts that actually look good, so I tested LF
> L125: For a local model on llama.cpp, give it one tool named `stone` that runs a stone command line, and put `skill/tier

## 星数曲线

```mermaid
xychart-beta
    title "Students-of-Local/smoothstone 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 81 --> 84
    line [82, 83]
```

2026-11-26 82 → 2026-11-28 83（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `44a1b9c3ee51` · [字段定义](../../DATASET.md)*
