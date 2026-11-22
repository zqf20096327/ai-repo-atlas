# alegauss/modelado

⭐ 3 · C# · Apache-2.0 · 推送 2026-11-16 · [GitHub](https://github.com/alegauss/modelado) · [官网](https://alegauss.com/modelado/) · 个人维护

**Windows 用户在本地把照片转成 3D 模型的 AI 应用**

Windows 桌面应用，把物体照片转成 3D 模型并编辑已有模型：3D 物体走 U²-Net 抠图加 TripoSR 重建，浮雕走 Depth Anything V2，纹理增强走 Real-ESRGAN，全部模型经 ONNX Runtime + DirectML 在本地 GPU 或 CPU 运行，照片不离开电脑。提供网格编辑（简化/细分/平滑/补洞/加厚等）、GLB/OBJ/STL/3MF/PLY 导出、命令行工具与 Blender 插件。模型首次使用时从 Hugging Face 下载并做 SHA-256 校验；Meshy AI/Ideogram 云服务为可选项，需自备 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 照片转 3D 物体（TripoSR）与浮雕（Depth Anything V2），本地运行不上传
- DirectML 路径支持 AMD/Intel/NVIDIA GPU，无显卡可回落 CPU
- 网格编辑工具集（简化、补洞、扁平底、厚度检查与加厚）面向 3D 打印
- CLI 与 Blender 插件，支持与 Blender 双向互传

## 适用场景

- 把物体照片变成可 3D 打印的模型并直接送入切片器
- 为游戏、Blender 或网页制作 3D 素材
- 修复与优化已有 3D 模型（补洞、简化、加厚、纹理锐化）

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: For anyone who wants to work in 3D with AI and save time: Modelado is a Windows app that turns
> L7: **No NVIDIA GPU needed.** Modelado runs its models through DirectML, so any DirectX 12 graphics
> L31: |**3D Object**|U²-Net (cut-out) → TripoSR (encoder + decoder) → marching cubes|A closed mesh with front, sides and 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `9a0bcf82c030` · [字段定义](../../DATASET.md)*
