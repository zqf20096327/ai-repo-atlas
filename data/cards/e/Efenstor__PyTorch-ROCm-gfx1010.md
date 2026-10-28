# Efenstor/PyTorch-ROCm-gfx1010

⭐ 24 · 推送 2026-05-10 · [GitHub](https://github.com/Efenstor/PyTorch-ROCm-gfx1010) · 个人维护

**在 Debian 12 上为 AMD gfx1010 显卡编译 PyTorch 2.8 的指令与补丁集**

面向 Radeon RX 5600/5700（gfx1010）用户的构建指南仓库：说明为何预编译二进制与 HSA_OVERRIDE 等技巧均不可用，给出从源码编译 PyTorch 2.8、TorchVision、TorchAudio 的完整步骤，附 composable_kernel 补丁与缺失的 RocBLAS TensileLibrary 文件。产物 wheel 经 chaiNNer 与 ComfyUI 测试。另含 Triton、bitsandbytes、xformers、Vulkan 后端等附加构建说明，其中部分标注为不可用或未验证；预编译 wheel 已不再提供（转向 Debian 13 版本仓库）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整的 PyTorch 2.8 gfx1010 源码构建流程（含 venv、补丁、CMake 参数）
- 提供 composable_kernel 编译补丁与 RocBLAS TensileLibrary 缺失文件
- TorchVision/TorchAudio/Triton/bitsandbytes/Vulkan 等附加组件构建说明与状态标注
- 构建产物经 chaiNNer 与 ComfyUI 使用测试

## 适用场景

- 在 RX 5600/5700 显卡的 Debian 12 机器上运行依赖 PyTorch 的应用（如 ComfyUI、chaiNNer）
- 解决 gfx1010 上预编译 PyTorch 二进制不可用的编译问题
- 排查 gfx1010 编译或运行报错（CMake 版本、警告即错误等）

## 场景标签

 · 领域:AI 基础设施/构建工具链

## 证据(README 行号)

> L27: These instructions are the result of the efforts to make PyTorch work with unofficially-supported AMD gfx1010 GPUs 
> L37: The only working solution seems to be is to build PyTorch and TorchVision from the source code with the support for
> L39: The resulting Python wheels were tested with chaiNNer and ComfyUI and both seem to work fine.

## 星数曲线

```mermaid
xychart-beta
    title "Efenstor/PyTorch-ROCm-gfx1010 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9fd43157ea46` · [字段定义](../../DATASET.md)*
