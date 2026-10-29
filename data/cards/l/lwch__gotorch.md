# lwch/gotorch

⭐ 69 · Go · MIT · 推送 2025-11-09 · [GitHub](https://github.com/lwch/gotorch) · 个人维护 · 中文 README

**Go 语言的 libtorch 绑定库：在 Go 中搭建与加载 PyTorch 模型**

通过 cgo 封装 libtorch（C++ PyTorch 后端）的 Go 库，提供张量创建（含 CUDA 设备）、模型 checkpoint 加载（读取 .pt 参数）等能力，支持 Windows/Linux/macOS 与 CPU/GPU 运算。安装需手动下载 libtorch 并配置库路径，Windows 下需额外通过 libgotorch 库衔接 msvc 编译的 libtorch 与 mingw 链接，cgo 依赖 mingw（推荐 llvm-mingw）。README 提示 tensor 在 C 栈创建，建议长期训练服务关闭 Go GC 并手动调用 runtime.GC。版本表跟踪 libtorch 2.0.1 至 2.9.x 的对应关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cgo 封装 libtorch，跟踪 libtorch 2.0.1~2.9.x 版本对应
- 支持 CPU 与 GPU（CUDA 设备）张量运算
- 支持加载模型 checkpoint 并遍历参数与形状
- Windows 下经 libgotorch 库衔接 msvc/mingw 链接差异

## 适用场景

- 在 Go 服务中加载并运行 PyTorch 训练的模型
- 用 Go 搭建与训练神经网络（如 mlp 示例）
- 需要 GPU 推理/训练且偏好 Go 技术栈的场景

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: 这是一个GO版本的libtorch封装库，通过该库可快速搭建torch的模型，目前已支持最新版本的libtorch(2.0.1)，支持的操作系统如下
> L13: 已支持*CPU*和*GPU*运算
> L68: m, _ := model.Load("yolo_tiny.pt", nil)

## 星数曲线

```mermaid
xychart-beta
    title "lwch/gotorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-29 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `75537997a680` · [字段定义](../../DATASET.md)*
