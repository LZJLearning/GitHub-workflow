# ------------------------------------------
# 文件路径: github-workflow/Dockerfile
# 编辑器: VSCode 中修改
# ------------------------------------------

# 1️⃣ 使用 Python 3.11 官方镜像
FROM python:3.11-slim

# 2️⃣ 在容器内创建工作目录
WORKDIR /app

# 3️⃣ 复制依赖文件并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ 复制整个项目到容器中
COPY . .

# 5️⃣ 添加 app 目录到 Python 模块搜索路径
ENV PYTHONPATH=/app

# 6️⃣ 测试 dedupe 模块是否可用
CMD ["python", "-c", "import app.dedupe; print('✅ dedupe module available')"]
